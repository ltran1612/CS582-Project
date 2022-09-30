# CS582-Project
An experiment to compare Cassandra vs MySQL


## Installation
    source setup.sh

## Configuration
    create config.py
    
    Add the below lines into config.py and update the key-pair with the right values.
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
