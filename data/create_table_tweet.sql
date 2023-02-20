DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    id              TEXT,
    user_fk         TEXT,
    created_at      TEXT,
    message         TEXT,
    image           TEXT,
    updated_at      TEXT,
    total_likes     TEXT,
    total_retweets  TEXT,
    total_views     TEXT,
    total_replies   TEXT,
    PRIMARY KEY(id)
)WITHOUT ROWID;

INSERT INTO tweets VALUES(
"489fbee271944245851514e94410b415", 
"8702b025cb1d4cd1be7d9eb41b46a152", 
"1676283558", 
"My first tweet", 
"", 
"", 
"0", 
"0", 
"0", 
"0"
);
