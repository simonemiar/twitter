-- PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id                TEXT NOT NULL UNIQUE,
    user_username          TEXT NOT NULL UNIQUE,
    user_email             TEXT NOT NULL UNIQUE,
    user_password          TEXT NOT NULL,
    user_first_name        TEXT NOT NULL,
    user_last_name         TEXT DEFAULT "",
    user_created_at        INTEGER NOT NULL,
    user_total_followers   INTEGER TEXT DEFAULT 0,
    user_total_following   INTEGER TEXT DEFAULT 0,
    user_total_tweets      INTEGER TEXT DEFAULT 0,
    user_total_retweets    INTEGER TEXT DEFAULT 0,
    user_avatar            TEXT,
    user_banner            TEXT,
    user_verified          BOOLEAN,
    user_verification_key  TEXT NOT NULL UNIQUE,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;


INSERT INTO users VALUES("8702b025cb1d4cd1be7d9eb41b46a152", "elonmusk", "a@a.dk", "MMDkodeord123", "Elon", "Musk", "1679498616", "128900000", "177", "22700", "22", "8702b025cb1d4cd1be7d9eb41b46a152.jpg", "1a1b274d5ad348a295bdd485b8be54db.jpeg", 1, "bc1324c4d3374550ac2f463422e78b9b");
INSERT INTO users VALUES("9873866baf6f462d874e019dc11cdfcc", "shakira", "b@b.dk", "MMDkodeord123", "Shakira", "", "1679498616", "53700000", "235", "7999", "112", "9873866baf6f462d874e019dc11cdfcc.jpg", "39fd798428b64497aa10ef206c931623.jpeg", 1, "b853c4df19dc4c5e9f97aa25b5277ac2");
INSERT INTO users VALUES("0891b4346ba74597a28a1ba171a3e60a", "rihanna", "c@c.dk", "MMDkodeord123", "Rihanna", "", "1679498616", "107900000", "980", "106000", "222", "0891b4346ba74597a28a1ba171a3e60a.jpg", "4bd8af77e616496794502b8de30b396d.jpeg", 1, "5b259b27e7014898980e73aa9c513194");
INSERT INTO users VALUES("441b0b988c024ccdb040c7948c46225e", "simonemiar", "s@s.dk", "MMDkodeord123", "Simone", "Kragh-Jacobsen", "1679498616", "2", "2", "5", "0", "8671046ba9204e9b8c821196a7e8987b.jpg", "default_banner.jpg", 1, "47a658e2a331444d96311af1f1994393");


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


INSERT INTO tweets VALUES("3b8511636d704d32ae7526d078b9469d", "8702b025cb1d4cd1be7d9eb41b46a152", "1686270744", "", "ade24070be174a3e8bef8253cb6cf963.jpeg", "", "15", "5", "2", "");
INSERT INTO tweets VALUES("66fca49de41b41e08882fb357cbc4997", "8702b025cb1d4cd1be7d9eb41b46a152", "1685665944", "Let that sink in", "", "", "679", "40", "894", "");
INSERT INTO tweets VALUES("ad433917bd1242448db3cdec8b3c8eee", "8702b025cb1d4cd1be7d9eb41b46a152", "1685665844", "x", "", "", "345", "20", "424", "");
INSERT INTO tweets VALUES("f875664a735c403fbf6fe53e532e742c", "8702b025cb1d4cd1be7d9eb41b46a152", "1685579544", "Congratulations to Giga Shanghai & Tesla China SDS teams for their excellent work overcoming many obstacles over many years!!", "6efaa4e8a41d4680ab2e22c65b054542.png", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("e12ffa66b9024a0f88788b217b81b79c", "8702b025cb1d4cd1be7d9eb41b46a152", "1684665844", "Consenting adults should do whatever makes them happy, provided it does not harm others, but a child is not capable of consent, which is why we have laws protecting minors", "", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("30cb1e98771b4d1e8d36b78bbf80ba97", "8702b025cb1d4cd1be7d9eb41b46a152", "1682987544", "Lil X just asked if there are police cats, since there are police dogs ", "", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("57437257dce64c0c9ff54158fc5bc40b", "8702b025cb1d4cd1be7d9eb41b46a152", "1685147544", "Also, you can now change video playback speed", "", "", "", "", "", "");
INSERT INTO tweets VALUES("fb6d972161654a7087d6e9852f651747", "8702b025cb1d4cd1be7d9eb41b46a152", "1682987544", "Scrolling through tweets while watching mini video (pic in pic) is great", "", "", "1", "", "3", "");
INSERT INTO tweets VALUES("bd4d9a129a85441994d15c3de37a90ee", "8702b025cb1d4cd1be7d9eb41b46a152", "1684888344", "What will AI be like in 2040?", "04f7432931ff4f0a8f4845df21d48888.jpeg", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("6af76dfe8e924dd2a4680f287deb40f8", "8702b025cb1d4cd1be7d9eb41b46a152", "1682987544", "z", "", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("08eec4384bd94e3095b15f0c1f9bef13", "8702b025cb1d4cd1be7d9eb41b46a152", "1682987544", "y", "", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("26864b1cf12848e284b9d9bf0d630e4a", "8702b025cb1d4cd1be7d9eb41b46a152", "1682987544", "My first tweet æver", "", "", "1", "2", "3", "");

INSERT INTO tweets VALUES("4a2c95fa7490448f9f937b0710cd6c9f", "0891b4346ba74597a28a1ba171a3e60a", "1685664944", "this shirt is old… @SavageXFenty", "8ba65741c27e4769a34404414fc53f77.png", "", "32", "19", "976", "");
INSERT INTO tweets VALUES("2a638c5b07424bcc84ecff9cde29cc37", "0891b4346ba74597a28a1ba171a3e60a", "1682987544", "Enjoying motherhood", "0891b4346ba74597a28a1ba171a3e60a.jpg", "", "1", "2", "3", "");
INSERT INTO tweets VALUES("66401e880f81472c85b44d8c8415eb4e", "0891b4346ba74597a28a1ba171a3e60a", "1682987544", "My first tweet", "", "", "1", "2", "3", "");

INSERT INTO tweets VALUES("a39dd044d34a4e809263dfb099269868", "9873866baf6f462d874e019dc11cdfcc", "1684247544", "After you", "9873866baf6f462d874e019dc11cdfcc.jpg", "", "37", "10", "876", "");
INSERT INTO tweets VALUES("ca77d83b778e49d1bbd21fbb6b6c39fa", "9873866baf6f462d874e019dc11cdfcc", "1681247544", "Before you", "ced730c558d0484595800479707e410b.jpeg", "", "1", "2", "3", "");

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