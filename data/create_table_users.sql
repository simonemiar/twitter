DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  user_username          TEXT,
  user_email             TEXT,
  user_password          TEXT,
  user_first_name        TEXT,
  user_last_name         TEXT,
  user_total_followers   TEXT,
  user_total_following   TEXT,
  user_total_tweets      TEXT,
  user_avatar            TEXT,
  user_hero_image        TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;


INSERT INTO users VALUES("8702b025cb1d4cd1be7d9eb41b46a152", "elonmusk", "a@a.dk", "123", "Elon", "Musk", "128900000", "177", "22700", "8702b025cb1d4cd1be7d9eb41b46a152.jpg", "1a1b274d5ad348a295bdd485b8be54db.jpeg");
INSERT INTO users VALUES("9873866baf6f462d874e019dc11cdfcc", "shakira", "b@b.dk", "123", "Shakira", "", "53700000", "235", "7999", "9873866baf6f462d874e019dc11cdfcc.jpg", "39fd798428b64497aa10ef206c931623.jpeg");
INSERT INTO users VALUES("0891b4346ba74597a28a1ba171a3e60a", "rihanna", "c@c.dk", "123", "Rihanna", "", "107900000", "980", "106000", "0891b4346ba74597a28a1ba171a3e60a.jpg", "4bd8af77e616496794502b8de30b396d.jpeg");
