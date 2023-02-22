# 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  # https://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@github.com/simonemiar/twitter.git
#######################
from bottle import get, post, run, view, template, static_file, response, request, default_app
import sqlite3
import git
import os

 
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./twitter')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 
##############################

# This data will come from the database
# For now, we just hard codedthe data
tweets = [
  { "verified": 1, "image_name":"1.jpg", "fullname":"Simone Kragh-Jacobsen", "username":"simonemiar","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"2.jpg", "fullname":"Rihanna", "username":"rihanna","message":"I am THE president","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"1.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"3.jpg", "fullname":"Shakira", "username":"shakira","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},

]

trends = [
  {"title": "One", "total_hashtags":1},
  {"title": "Two", "total_hashtags":2},
  {"title": "Tree", "total_hashtags":3},
  {"title": "Four", "total_hashtags":4},
  {"title": "Five", "total_hashtags":5},
]

follows =  [
  {"image_name":"1.jpg", "fullname": "Elon Musk", "username": "elonmusk"},
  {"image_name":"2.jpg", "fullname": "Joe Biden", "username": "joebiden"},
  {"image_name":"3.jpg", "fullname": "Shakira", "username": "shakira"},
]

##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/thumbnails/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/thumbnails/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/")
def render_index():
  return template("index", title="Twitter", tweets=tweets, trends=trends, follows=follows, server="paste")



##############################

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
# profile page setup 

@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(os.getcwd()+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE",(username,)).fetchall()[0]
    # Get the user's id
    user_id = user["id"]
    print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
    print(tweets)
    # pass the tweets to the view. Template it
    
    print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user, trends=trends)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()

##############################

try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=5000, debug=True, reloader=True)