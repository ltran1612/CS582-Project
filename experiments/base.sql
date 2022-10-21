CREATE TABLE youtube(
video_id NVARCHAR(20) NOT NULL Primary key,
title NVARCHAR(100) NULL,
publishedAt NVARCHAR(30) NULL,
channelId NVARCHAR(50) NULL,
channelTitle NVARCHAR(20) NULL,
categoryId NVARCHAR(20) NULL,
trending_date NVARCHAR(30) NULL,
tags NVARCHAR(1000) NULL,
view_count INT NULL,
likes INT NULL,
dislikes INT NULL,
comment_count INT NULL,
thumbnail_linke VARCHAR(500) NULL,
comments_disabled NVARCHAR(7) NULL,
ratings_disabled NVARCHAR(7) NULL,
desciption NVARCHAR(5000) NULL
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