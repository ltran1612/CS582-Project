CREATE KEYSPACE test
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};

USE test;
SELECT * from netflix;

USE test;
CREATE TABLE netflix(
showid text PRIMARY KEY,
type text,
title text,
director text,
cast text,
country text,
date_added text,
release_year int,
rating text,
duration text,
listed_in text,
description text
);

USE test;
CREATE TABLE youtube(
video_id text NOT NULL Primary key,
title text NULL,
publishedAt text NULL,
channelId text NULL,
channelTitle text NULL,
categoryId text NULL,
trending_date text NULL,
tags text NULL,
view_count INT NULL,
likes INT NULL,
dislikes INT NULL,
comment_count INT NULL,
thumbnail_linke text NULL,
comments_disabled text NULL,
ratings_disabled text NULL,
desciption text NULL
);

COPY test.netflix
FROM ''
WITH DELIMITER = ','
;

COPY test.youtube
FROM '/Users/longtran/Personal/Computer Science/CS582/youtube/BR_youtube_trending_data.csv'
WITH DELIMITER = ','
AND HEADER=TRUE
;
