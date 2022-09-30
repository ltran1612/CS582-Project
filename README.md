# CS582-Project
An experiment to compare Cassandra vs MySQL


## Installation
    source setup.sh

## Configuration

1) Create the file config.py
    
2) Add the below lines into config.py and update the key-pair with the right values:

        MYSQL_CONFIG = {
          "user": "root",
          "password": "1234",
          "ip_address": "127.0.0.1"
        }

        CASSANDRA_CONFIG = {
          "user": "root",
          "password": "",
          "ip_address": "127.0.0.1"
        }
