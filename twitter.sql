-- PRAGMA foreign_keys = ON;

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
    user_logged_in         BOOLEAN,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;


INSERT INTO users VALUES("8702b025cb1d4cd1be7d9eb41b46a152", "elonmusk", "a@a.dk", "123", "Elon", "Musk", "1679498616", "128900000", "177", "22700", "22", "8702b025cb1d4cd1be7d9eb41b46a152.jpg", "1a1b274d5ad348a295bdd485b8be54db.jpeg", 1, "bc1324c4d3374550ac2f463422e78b9b", 0);
INSERT INTO users VALUES("9873866baf6f462d874e019dc11cdfcc", "shakira", "b@b.dk", "123", "Shakira", "", "1679498616", "53700000", "235", "7999", "112", "9873866baf6f462d874e019dc11cdfcc.jpg", "39fd798428b64497aa10ef206c931623.jpeg", 1, "b853c4df19dc4c5e9f97aa25b5277ac2", 0);
INSERT INTO users VALUES("0891b4346ba74597a28a1ba171a3e60a", "rihanna", "c@c.dk", "123", "Shakira", "", "1679498616", "107900000", "980", "106000", "222", "0891b4346ba74597a28a1ba171a3e60a.jpg", "4bd8af77e616496794502b8de30b396d.jpeg", 1, "5b259b27e7014898980e73aa9c513194", 0);
INSERT INTO users VALUES("441b0b988c024ccdb040c7948c46225e", "simonemiar", "s@s.dk", "123", "Simone", "Kragh-Jacobsen", "1679498616", "2", "2", "5", "0", "0891b4346ba74597a28a1ba171a3e60a.jpg", "cbfc2c6a2b4a48d1b76854ebc6b002ba.jpeg", 1, "47a658e2a331444d96311af1f1994393", 0);


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
) WITHOUT ROWID;


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


-- SELECT * FROM tweets


-- -- this is to see all my Triggers in a table by name 
-- SELECT name FROM sqlite_master WHERE type = 'trigger';
-- -- this is to see all my Indexes in a table by name 
-- SELECT name FROM sqlite_master WHERE type = 'index';

-- DROP TRIGGER IF EXISTS increment_user_total_tweets;
-- CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
-- BEGIN
--   UPDATE users 
--   SET user_total_tweets =  user_total_tweets + 1 
--   WHERE user_id = NEW.tweet_user_fk;
-- END;
-- DROP TRIGGER IF EXISTS decrement_user_total_tweets;
-- CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
-- BEGIN
--   UPDATE users 
--   SET user_total_tweets =  user_total_tweets - 1 
--   WHERE user_id = OLD.tweet_user_fk;
-- END;