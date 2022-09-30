source env/bin/activate
docker run -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mysql
