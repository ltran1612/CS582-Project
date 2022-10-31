import pandas as pd

def insert_to_cassandra(cassandra):
    insert_stmt = "INSERT INTO youtube (id, video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, desciption) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')
    print(df.columns.tolist())
    count = 0
    buffer_size = 0
    for index, row in df.iterrows():
        cassandra.execute("use test;")
        #row['description'] = ""
        #row['title'] = ""
        #row["tags"] = ""
        row['categoryId'] = str(row['categoryId'])
        row['comments_disabled'] = str(row['comments_disabled'])
        row['ratings_disabled'] = str(row['ratings_disabled'])
        row['description'] = str(row['description'])
        #row["channelTitle"] = ""
        data = list(row) #(row['video_id'], row['title'], row['publishedAt'], row['channelId'], row['channelTitle'], row[''])
        data = [count] + data
        result = cassandra.execute(insert_stmt, data)
        count = count + 1
        buffer_size = buffer_size + 1
        #print("inserted", count)
    print(count)

def insert_to_mysql(mysql_connect, mysql):
    insert_stmt = ("INSERT INTO youtube (id, video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')
    print(df.columns.tolist())
    count = 0
    buffer_size = 0
    mysql.execute("use test;")
    for index, row in df.iterrows():
        row['description'] = str(row['description'])
        row['title'] = str(row['title'])
        row["tags"] = str(row["tags"])
        row["channelTitle"] = str(row["channelTitle"])
        data = list(row) #(row['video_id'], row['title'], row['publishedAt'], row['channelId'], row['channelTitle'], row[''])
        data = [count] + data
        #print(len(data))
        mysql.execute(insert_stmt, data)
        count = count + 1
        buffer_size = buffer_size + 1
        #print("inserted", count)
        if buffer_size > 500:
            mysql_connect.commit()
            buffer_size = 0
            print("commited 500")
    mysql_connect.commit()
    print(count)



