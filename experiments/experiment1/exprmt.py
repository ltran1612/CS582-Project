from misc import get_queries, Timer, debug

def runExperiment1(mysql, cassandra, iterations=1):
    mysql_queries_row = get_queries("experiments/experiment1/experiment1_row.sql")
    cassandra_queries_row = get_queries("experiments/experiment1/experiment1_row.cql")
    mysql_queries_column = get_queries("experiments/experiment1/experiment1_col.sql")
    cassandra_queries_column = get_queries("experiments/experiment1/experiment1_col.cql")

    print("mysql-row, mysql-column, cassandra-row, cassandra-column")
    for i in range(iterations):
        # execute mysql queries
        timer = Timer()
        timer.start()
        for query in mysql_queries_row: 
            mysql.execute(query)
        mysql_time_row = timer.stop()

        timer.start()
        for query in mysql_queries_column: 
            mysql.execute(query)
        mysql_time_column = timer.stop()

        # execute cassandra queries
        timer.start()
        for query in cassandra_queries_row:
            rows = cassandra.execute(query)
        cassandra_time_row = timer.stop()

        timer.start()
        for query in cassandra_queries_column:
            rows = cassandra.execute(query)
        cassandra_time_column = timer.stop()

        print("{},{},{},{}".format(mysql_time_row, mysql_time_column, cassandra_time_row, cassandra_time_column))