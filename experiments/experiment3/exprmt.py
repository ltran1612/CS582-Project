from misc import get_queries, Timer, debug

def runExperiment3(mysql, cassandra, iterations=1):
    mysql_queries = get_queries("experiments/experiment3/experiment3.sql")
    cassandra_queries = get_queries("experiments/experiment3/experiment3.cql")
    mysql_create_index = get_queries("experiments/experiment3/experiment3_create_index.sql")
    cassandra_create_index = get_queries("experiments/experiment3/experiment3_create_index.cql")
    mysql_drop_index = get_queries("experiments/experiment3/experiment3_drop_index.sql") 
    cassandra_drop_index = get_queries("experiments/experiment3/experiment3_drop_index.cql") 

    mysql.execute("use test11;")
    cassandra.execute("use test;")

    

    print("mysql-with-index, mysql-no-index, cassandra-with-index, cassandra-no-index")

    for query in mysql_drop_index:
            mysql.execute(query)

    for i in range(iterations):
        # execute mysql queries
        timer = Timer()
        timer.start()
        for query in mysql_queries: 
            #debug(query)
            try:
                mysql.execute(query)
                #debug(mysql.rowcount)
            except Exception as e:
                debug(e)
        mysql_no_index = timer.stop()

        for query in mysql_create_index:
            mysql.execute(query)

        timer = Timer()
        timer.start()
        for query in mysql_queries: 
            #debug(query)
            try:
                mysql.execute(query)
                #debug(mysql.rowcount)
            except Exception as e:
                debug(e)
        mysql_with_index = timer.stop()

        for query in cassandra_drop_index:
            cassandra.execute(query)

        # execute cassandra queries
        timer = Timer()
        timer.start()
        for query in cassandra_queries:
            #debug(query)
            try:
                rows = cassandra.execute(query)
                #debug(len(rows.all()))
            except Exception as e:
                debug(e)
        cassandra_no_index = timer.stop()

        for query in cassandra_create_index:
            cassandra.execute(query)

        timer = Timer()
        timer.start()
        for query in cassandra_queries:
            #debug(query)
            try:
                rows = cassandra.execute(query)
                #debug(len(rows.all()))
            except Exception as e:
                debug(e)
        cassandra_with_index = timer.stop()

        print("{},{},{},{}".format(mysql_with_index, mysql_no_index, cassandra_with_index, cassandra_no_index))
