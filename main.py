from cassandra.cluster import Cluster
import mysql.connector
from config import *
import sys
from misc import *
from experiments.experiment1.exprmt import runExperiment1
from experiments.experiment3.exprmt import runExperiment3
from experiments.experiment2.exprmt import runExperiment2
from experiments.experiment4.exprmt import runExperiment4
from insert import *

# The entry to the test program
# Precondition:
# Postcondition:

if __name__ == "__main__":
    # Connecting to databases
    print("-"*16 + "CONNECTING TO DATABASES..." + "-"*16)

    cassandra_cluster = Cluster([CASSANDRA_CONFIG['ip_address']])
    cassandra_session = cassandra_cluster.connect()
    my_sql_cnx = mysql.connector.connect(
        user=MYSQL_CONFIG['user'], password=MYSQL_CONFIG["password"],
        host=MYSQL_CONFIG['ip_address']
    )
    mysql_cursor = my_sql_cnx.cursor(dictionary=True, buffered=True)
    print("-"*16 + "CONNECTED TO DATABASES" + "-"*16)


    # Choose and execute the experiment
    while True:
        experiment_num = input("""
CHOOSE AN EXPERIMENT: 
    1) Row-oriented vs Column Oriented
    2) Insertion Time Comparision (without index)
    3) Query with index vs Query without index.  
    4) Insertion Time Comparison (with index)
    5) Insert YouTube data to MySQL
    6) Insert YouTube data Cassandra
""")
    
        if experiment_num == "1":
            run_experiment(mysql_cursor, cassandra_session, runExperiment1)
        elif experiment_num == "2":
            run_experiment(my_sql_cnx, cassandra_session, runExperiment2)
        elif experiment_num == "3":
            run_experiment(mysql_cursor, cassandra_session, runExperiment3)
        elif experiment_num == "4":
            run_experiment(mysql_cursor, cassandra_session, runExperiment4)
        elif experiment_num == "5":
            insert_to_mysql(my_sql_cnx, mysql_cursor)
        elif experiment_num == "6":
            insert_to_cassandra(cassandra_session)
        else:
            pass

