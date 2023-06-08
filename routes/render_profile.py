from bottle import get, request, template
import x
import os
import sqlite3
import traceback
##############################
# profile page setup 

trends = [
    {"title": "#RENAISSANCETOUR", "total_hashtags":1},
    {"title": "StarWars", "total_hashtags":2},
    {"title": "#Web3", "total_hashtags":4.23},
    {"title": "dkpol", "total_hashtags":1.576},
    {"title": "politidk", "total_hashtags":243},
]

follows =  [
  {"image_name":"8702b025cb1d4cd1be7d9eb41b46a152.jpg", "fullname": "Elon Musk", "username": "elonmusk"},
  {"image_name":"0891b4346ba74597a28a1ba171a3e60a.jpg", "fullname": "Rihanna", "username": "rihanna"},
  {"image_name":"9873866baf6f462d874e019dc11cdfcc.jpg", "fullname": "Shakira", "username": "shakira"},
]

@get("/<user_username>")
# @view("profile")
def _(user_username):
    try:
        # get logged in user
        print(user_username)
        get_user = request.get_cookie("user", secret="my-secret")
        if get_user:
            user = get_user[0]
        else:
            user = None
        
        print("username", user_username)
        db = sqlite3.connect(os.getcwd()+"/twitter.db")
        db.row_factory = x.dict_factory
        profile = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE",(user_username,)).fetchone()
        print(profile)

        # Get the user's id
        user_id = profile['user_id']
        print(f"user id:{user_id}")
        # With that id, look up/get the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweet_created_at DESC LIMIT 10", (user_id,)).fetchall()
        # print(tweets)
        # pass the tweets to the view. Template it
        
        # print("visited user profile", user_profile) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
        return template("profile", title="Twitter", profile=profile, user=user, trends=trends, tweets=tweets, follows=follows)
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
        traceback.print_exc()
        return "error"
    finally:
        if "db" in locals(): db.close()

##############################