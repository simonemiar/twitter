DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    tweet_id              TEXT,
    tweet_user_fk         TEXT,
    tweet_created_at      TEXT,
    tweet_message         TEXT,
    tweet_image           TEXT,
    tweet_updated_at      TEXT,
    tweet_total_replies   TEXT,
    tweet_total_likes     TEXT,
    tweet_total_retweets  TEXT,
    tweet_total_views     TEXT,
    PRIMARY KEY(tweet_id)
)WITHOUT ROWID;

INSERT INTO tweets VALUES(
"489fbee2", 
"8702b025cb1d4cd1be7d9eb41b46a152", 
"1676283558", 
"My first tweet æver", 
"", 
"1/1/2000", 
"1", 
"2", 
"3", 
"4"
);


