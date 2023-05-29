PRAGMA foreign_keys=ON

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id                TEXT NOT NULL UNIQUE,
    user_username          TEXT NOT NULL UNIQUE,
    user_email             TEXT NOT NULL,
    user_password          TEXT NOT NULL,
    user_first_name        TEXT NOT NULL,
    user_last_name         TEXT DEFAULT "",
    user_created_at        INTEGER NOT NULL,
    user_total_followers   INTEGER TEXT DEFAULT 0,
    user_total_following   INTEGER TEXT DEFAULT 0,
    user_total_tweets      INTEGER TEXT DEFAULT 0,
    user_total_retweets    INTEGER TEXT DEFAULT 0,
    user_avatar            TEXT,
    user_banner            TEXT UNIQUE,
    user_verified          BOOLEAN,
    user_verification_key  TEXT NOT NULL UNIQUE,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;


INSERT INTO users VALUES("8702b025cb1d4cd1be7d9eb41b46a152", "elonmusk", "a@a.dk", "123", "Elon", "Musk", "1679498616", "128900000", "177", "22700", "22", "8702b025cb1d4cd1be7d9eb41b46a152.jpg", "1a1b274d5ad348a295bdd485b8be54db.jpeg", 1, "bc1324c4d3374550ac2f463422e78b9b");
INSERT INTO users VALUES("9873866baf6f462d874e019dc11cdfcc", "shakira", "b@b.dk", "123", "Shakira", "", "1679498616", "53700000", "235", "7999", "112", "9873866baf6f462d874e019dc11cdfcc.jpg", "39fd798428b64497aa10ef206c931623.jpeg", 1, "b853c4df19dc4c5e9f97aa25b5277ac2");
INSERT INTO users VALUES("0891b4346ba74597a28a1ba171a3e60a", "rihanna", "c@c.dk", "123", "Rihanna", "", "1679498616", "107900000", "980", "106000", "222", "0891b4346ba74597a28a1ba171a3e60a.jpg", "4bd8af77e616496794502b8de30b396d.jpeg", 1, "5b259b27e7014898980e73aa9c513194");



DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    tweet_id              TEXT,
    tweet_user_fk         TEXT,
    tweet_created_at      INTEGER,
    tweet_message         TEXT,
    tweet_image           TEXT,
    tweet_updated_at      TEXT,
    tweet_total_replies   TEXT,
    tweet_total_likes     TEXT,
    tweet_total_retweets  TEXT,
    tweet_total_views     TEXT,
    PRIMARY KEY(tweet_id),
    FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)
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


-- INSERT INTO TWEETS VALUES("8702b025cb1d4cd1be7d9eb41b46a153", "xxx", "1676283558", "xxx", "", "1", "", "1/1/2000", "1", "2")

SELECT * FROM tweets

