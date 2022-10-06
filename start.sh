source env/bin/activate
docker run -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mysql
docker run -p 9042:9042 -d cassandra:3.11
