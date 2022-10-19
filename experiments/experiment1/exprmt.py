from misc import get_queries, Timer, debug

def runExperiment1(mysql, cassandra, iterations=1):
    mysql_queries = get_queries("experiments/experiment1/experiment1_row.sql")
    cassandra_queries = get_queries("experiments/experiment1/experiment1_row.cql")

    print("mysql, cassandra")
    for i in range(iterations):
        # execute mysql queries
        timer = Timer()
        timer.start()
        for query in mysql_queries: 
            mysql.execute(query)
            result = mysql
            if result.with_rows:
                debug("Row count: ", result.rowcount)
                #debug(result.fetchall())
        mysql_time = timer.stop()

        # execute cassandra queries
        timer.start()
        for query in cassandra_queries:
            rows = cassandra.execute(query)
            debug("Row count: ", len(rows.all()))
        cassandra_time = timer.stop()

        print("{},{}".format(mysql_time, cassandra_time))