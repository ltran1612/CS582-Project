import pandas as pd
from misc import debug

def insert_to_cassandra(cassandra):    
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')
    #print(df.columns.tolist())

    rows = parse_data_for_cassandra(df)
    cassandra.execute("use test;")
    print("inserting...")
    insert_to_cassandra_test(cassandra, rows)

def parse_data_for_cassandra(df):
    count = 0
    rows = []
    for index, row in df.iterrows():
        row['categoryId'] = str(row['categoryId'])
        row['comments_disabled'] = str(row['comments_disabled'])
        row['ratings_disabled'] = str(row['ratings_disabled'])
        row['description'] = str(row['description'])
        data = list(row)
        data = [count] + data
        rows.append(data)
        count = count + 1
    return rows

def insert_to_cassandra_test(cassandra, rows):
    insert_stmt = "INSERT INTO youtube (id, video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, desciption) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for row in rows:
        result = cassandra.execute(insert_stmt, row)

def parse_data_for_mysql(df):
    count = 0
    rows = []
    for index, row in df.iterrows():
        row['description'] = str(row['description'])
        row['title'] = str(row['title'])
        row["tags"] = str(row["tags"])
        row["channelTitle"] = str(row["channelTitle"])
        data = list(row) 
        data = [count] + data
        rows.append(data)
        count = count + 1
    return rows

def insert_to_mysql_test(mysql_connect, mysql, rows):
    insert_stmt = ("INSERT INTO youtube (id, video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    buffer_size = 0
    
    for row in rows:
        mysql.execute(insert_stmt, row)
        buffer_size = buffer_size + 1

        if buffer_size > 10000:
            mysql_connect.commit()
            buffer_size = 0
            #debug("commited 1000")
    mysql_connect.commit()

def insert_to_mysql(mysql_connect, mysql):
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')
    #print(df.columns.tolist())
    rows = parse_data_for_mysql(df)
    mysql.execute("use test11;")
    print("inserting...")
    insert_to_mysql_test(mysql_connect, mysql, rows)



