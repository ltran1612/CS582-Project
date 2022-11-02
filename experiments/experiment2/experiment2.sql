use test11;
drop table youtube;
CREATE TABLE youtube(
id INT primary key,
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