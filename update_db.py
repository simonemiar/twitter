import bcrypt
import x

db = x.db()
salt = bcrypt.gensalt()

# user
user1 = db.execute("SELECT * FROM users WHERE user_email= 'a@a.dk' ").fetchone()
pw = bcrypt.hashpw(user1['user_password'].encode('utf-8'), salt)
db.execute(f"UPDATE users SET user_password=? WHERE user_email = 'a@a.dk'", (pw,))

# # user
# user2 = db.execute("SELECT * FROM users WHERE user_email= 'b@b.dk' ").fetchone()
# pw = bcrypt.hashpw(user2['user_password'].encode('utf-8'), salt)
# db.execute(f"UPDATE users SET user_password=? WHERE user_email = 'b@b.dk'", (pw,))

# # user
# user3 = db.execute("SELECT * FROM users WHERE user_email= 'c@c.dk' ").fetchone()
# pw = bcrypt.hashpw(user3['user_password'].encode('utf-8'), salt)
# db.execute(f"UPDATE users SET user_password=? WHERE user_email = 'c@c.dk'", (pw,))

# # user
# user4 = db.execute("SELECT * FROM users WHERE user_email= 's@s.dk' ").fetchone()
# pw = bcrypt.hashpw(user4['user_password'].encode('utf-8'), salt)
# db.execute(f"UPDATE users SET user_password=? WHERE user_email = 's@s.dk'", (pw,))





# users = db.execute("SELECT * FROM users WHERE user_password= 'MMDkodeord123' ").fetchall()

# for user in users:
#     print(user)
#     salt = bcrypt.gensalt()
#     pw = bcrypt.hashpw(user['user_password'].encode('utf-8'), salt)
#     db.execute(f"UPDATE users SET user_password=? WHERE user_password = 'MMDkodeord123'", (pw,))

    
db.commit()
db.close()