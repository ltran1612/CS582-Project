from cassandra.cluster import Cluster
import mysql.connector
from config import *

# The entry to the test program
# Precondition:
# Postcondition:

if __name__ == "__main__":
    print("-"*16 + "START EXPERIMENT" + "-"*16)
    cassandra_cluster = Cluster()
    my_sql_cnx = mysql.connector.connect(
        user=MYSQL_CONFIG['user'], password=MYSQL_CONFIG["password"],
        host=MYSQL_CONFIG['ip_address'],
        database=''
    )