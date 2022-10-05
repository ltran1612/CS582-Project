from cassandra.cluster import Cluster
import mysql.connector
from config import *
import sys

# The entry to the test program
# Precondition:
# Postcondition:

if __name__ == "__main__":
    print("-"*16 + "CONNECTING TO DATABASE..." + "-"*16)

    cassandra_cluster = Cluster([CASSANDRA_CONFIG.ip_address])
    my_sql_cnx = mysql.connector.connect(
        user=MYSQL_CONFIG['user'], password=MYSQL_CONFIG["password"],
        host=MYSQL_CONFIG['ip_address']
    )

    print("-"*16 + "CONNECTED TO DATABASE" + "-"*16)
    print("\n\n")
    while True:
        experiment_num = input("""CHOOSE AN EXPERIMENT: 
        1) 
        2)
        3) 
        4) 
        """)
    
        if experiment_num == 1:
            pass
        elif experiment_num == 2:
            pass
        elif experiment_num == 3:
            pass
        else:
            pass

