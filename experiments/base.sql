use test;
drop table youtube;
CREATE TABLE youtube(
video_id VARCHAR(20) NOT NULL,
title VARCHAR(100) 
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci,
publishedAt VARCHAR(30),
channelId VARCHAR(50),
channelTitle VARCHAR(70)
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci,
categoryId VARCHAR(20),
trending_date VARCHAR(30),
tags VARCHAR(1000) 
	CHARACTER SET utf8mb4
      COLLATE utf8mb4_unicode_ci,
view_count INT,
likes INT,
dislikes INT,
comment_count INT,
thumbnail_link VARCHAR(500),
comments_disabled VARCHAR(7),
ratings_disabled VARCHAR(7),
description VARCHAR(5000) 
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci
);

CREATE TABLE netflix
(
showid NVARCHAR(5) NOT NULL PRIMARY KEY,
type NVARCHAR(20) NULL ,
title NVARCHAR(100) NULL,
director NVARCHAR(50) NULL,
cast NVARCHAR(500) NULL,
country NVARCHAR(20) NULL,
date_added NVARCHAR(50) NULL,
release_year INT NULL,
rating NVARCHAR(10) NULL,
duration NVARCHAR(10) NULL,
listed_in NVARCHAR(50) NULL,
description NVARCHAR(500) NULL);

load data local infile '/Users/longtran/Personal/Computer Science/CS582/youtube/US_youtube_trending_data.csv' 
into table youtube
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(video_id, title, publishedAt,channelId,channelTitle,categoryId, trending_date,tags,view_count,likes,dislikes,comment_count,thumbnail_linke,comments_disabled,ratings_disabled,desciption)

load data local infile '/Users/longtran/Personal/Computer Science/CS582/netflix_titles.csv' 
into table netflix
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(showid, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)