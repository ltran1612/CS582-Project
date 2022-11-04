USE test;
drop table youtube;

CREATE TABLE test.youtube(
	id int primary key,
	video_id text,
	title text ,
	publishedAt text ,
	channelId text ,
	channelTitle text ,
	categoryId text,
	trending_date text ,
	tags text ,
	view_count INT ,
	likes INT ,
	dislikes INT ,
	comment_count INT ,
	thumbnail_link text ,
	comments_disabled text ,
	ratings_disabled text ,
	desciption text 
);

CREATE INDEX view_count_idx ON test.youtube(view_count);