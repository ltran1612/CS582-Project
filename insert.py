import pandas as pd

def insert_to_cassandra(cassandra):
    insert_stmt = "INSERT INTO youtube (video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_linke, comments_disabled, ratings_disabled, desciption) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
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
        data = tuple(row) #(row['video_id'], row['title'], row['publishedAt'], row['channelId'], row['channelTitle'], row[''])
        cassandra.execute(insert_stmt, data)
        count = count + 1
        buffer_size = buffer_size + 1
        #print("inserted", count)
    print(count)

def insert_to_mysql(mysql_connect, mysql):
    insert_stmt = ("INSERT INTO youtube (video_id, title, publishedAt, channelId, channelTitle, categoryId, trending_date, tags, view_count, likes, dislikes, comment_count, thumbnail_linke, comments_disabled, ratings_disabled, desciption) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    
    df = pd.read_csv('data/youtube/US_youtube_trending_data.csv')
    print(df.columns.tolist())
    count = 0
    buffer_size = 0
    for index, row in df.iterrows():
        mysql.execute("use test;")
        row['description'] = ""
        row['title'] = ""
        row["tags"] = ""
        row["channelTitle"] = ""
        data = tuple(row) #(row['video_id'], row['title'], row['publishedAt'], row['channelId'], row['channelTitle'], row[''])
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



