from misc import get_queries, Timer, debug

def runExperiment1(mysql, cassandra, iterations=1):
    mysql_queries_row = get_queries("experiments/experiment1/experiment1_row.sql")
    cassandra_queries_row = get_queries("experiments/experiment1/experiment1_row.cql")
    mysql_queries_column = get_queries("experiments/experiment1/experiment1_col.sql")
    cassandra_queries_column = get_queries("experiments/experiment1/experiment1_col.cql")
    
    print("mysql-row, mysql-column, cassandra-row, cassandra-column")
    for i in range(iterations):
        mysql.execute("use test;")
        cassandra.execute("use test;")
        # execute mysql queries
        timer = Timer()
        timer.start()
        for query in mysql_queries_row: 
            #debug(query)
            try:
                mysql.execute(query)
                #debug(mysql.rowcount)
            except Exception as e:
                debug(e)
        mysql_time_row = timer.stop()
        #debug(mysql_time_row)

        timer = Timer()
        timer.start()
        for query in mysql_queries_column: 
            #debug(query)
            try:
                mysql.execute(query)
                #debug(mysql.rowcount)
            except Exception as e:
                debug(e)
        mysql_time_column = timer.stop()
        #debug(mysql_time_column)

        # execute cassandra queries
        timer = Timer()
        timer.start()
        for query in cassandra_queries_row:
            #debug(query)
            try:
                rows = cassandra.execute(query)
                #debug(len(rows.all()))
            except Exception as e:
                debug(e)
        cassandra_time_row = timer.stop()
        #debug(cassandra_time_row)

        timer = Timer()
        timer.start()
        for query in cassandra_queries_column:
            #debug(query)
            try:
                rows = cassandra.execute(query)
                #debug(len(rows.all()))
            except Exception as e:
                debug(e)
        cassandra_time_column = timer.stop()
        #debug(cassandra_time_column)

        print("{},{},{},{}".format(mysql_time_row, mysql_time_column, cassandra_time_row, cassandra_time_column))