DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  first_name        TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  avatar            TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;


INSERT INTO users VALUES("8702b025cb1d4cd1be7d9eb41b46a152", "elonmusk", "Elon", "Musk", "128900000", "177", "22700", "8702b025cb1d4cd1be7d9eb41b46a152.jpg");
INSERT INTO users VALUES("9873866baf6f462d874e019dc11cdfcc", "shakira", "Shakira", "", "53700000", "235", "7999", "9873866baf6f462d874e019dc11cdfcc.jpg");
INSERT INTO users VALUES("0891b4346ba74597a28a1ba171a3e60a", "rihanna", "Rihanna", "", "107900000", "980", "106000", "0891b4346ba74597a28a1ba171a3e60a.jpg");
