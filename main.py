from cassandra.cluster import Cluster
import mysql.connector
from config import *
import sys
from misc import *
from experiments.experiment1.exprmt import runExperiment1

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
    2)
    3) 
    4) 
""")
    
        if experiment_num == "1":
            run_experiment(mysql_cursor, cassandra_session, runExperiment1)
        elif experiment_num == "2":
            pass
        elif experiment_num == "3":
            pass
        else:
            pass

