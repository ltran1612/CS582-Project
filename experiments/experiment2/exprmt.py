from misc import get_queries, Timer, debu
from insert import insert_to_cassandra_test, insert_to_mysql_test, parse_data_for_cassandra, parse_data_for_mysql
import pd

def runExperiment2(mysql_cnx, mysql_cursor, cassandra, iterations=1):
    print("mysql-time, cassandra-time")
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')

    mysql_data = parse_data_for_mysql(df)
    cassandra_data = parse_data_for_cassandra(df)

    for i in range(iterations):
        mysql_cursor.execute("use test11;")
        cassandra.execute("use test;")
        mysql_cursor.execute("drop table youtube;")
        cassandra.execute("drop table youtube;")
        
        # execute mysql queries
        timer = Timer()
        timer.start()
        insert_to_mysql_test(mysql_cnx, mysql_cursor, mysql_data)
        mysql_time = timer.stop()

        timer = Timer()
        timer.start()
        insert_to_cassandra_test(cassandra, cassandra_data)
        cassandra_time = timer.stop()

        print("{},{}".format(mysql_time, cassandra_time))