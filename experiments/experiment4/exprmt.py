from misc import get_queries, Timer, debug
from insert import insert_to_cassandra_test, insert_to_mysql_test, parse_data_for_cassandra, parse_data_for_mysql
import pandas as pd

def runExperiment4(mysql_cnx, cassandra, iterations=1):
    mysql_cursor = mysql_cnx.cursor(dictionary=True, buffered=True)
    print("mysql-time, cassandra-time")
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')

    mysql_queries = get_queries("experiments/experiment4/experiment4.sql")
    cassandra_queries = get_queries("experiments/experiment4/experiment4.cql")

    mysql_data = parse_data_for_mysql(df)
    cassandra_data = parse_data_for_cassandra(df)

    for i in range(iterations):
        for query in mysql_queries:
            debug(query)
            mysql_cursor.execute(query)
        for query in cassandra_queries:
            debug(query)
            cassandra.execute(query)
        
        # execute mysql queries
        debug("Inserting.. - mysql")
        timer = Timer()
        timer.start()
        insert_to_mysql_test(mysql_cnx, mysql_cursor, mysql_data)
        mysql_time = timer.stop()

        debug("Inserting.. - cassandra")
        timer = Timer()
        timer.start()
        insert_to_cassandra_test(cassandra, cassandra_data)
        cassandra_time = timer.stop()

        print("{},{}".format(mysql_time, cassandra_time))