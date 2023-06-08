# 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  # https://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@github.com/simonemiar/twitter.git
#######################
from bottle import get, post, run, view, template, static_file, response, request, default_app
import sqlite3
import git
import os
import x
import traceback

import apis.api_tweet
import apis.api_sign_up
import apis.api_follow
import apis.api_forgot_password
import apis.api_reset_password
import apis.api_login
import apis.api_deactivate_user_email
import apis.api_deactivate_user
import apis.api_upload_avatar

import bridges.logout

import routes.render_test
import routes.render_login
import routes.render_signup
import routes.render_verified
import routes.render_forgot_password
import routes.render_reset_password
import routes.render_deactivate_user
import routes.render_profile
##############################

@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")

 
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
fake_tweets = [
  { "verified": 1, "image_name":"8671046ba9204e9b8c821196a7e8987b.jpg", "fullname":"Simone Kragh-Jacobsen", "username":"simonemiar","message":"lol","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"0891b4346ba74597a28a1ba171a3e60a.jpg", "fullname":"Rihanna", "username":"rihanna","message":"I am THE president","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"8702b025cb1d4cd1be7d9eb41b46a152.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified": 1, "image_name":"9873866baf6f462d874e019dc11cdfcc.jpg", "fullname":"Shakira", "username":"shakira","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
]

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
  response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
  response.add_header("Pragma", "no-cache")
  response.add_header("Expires", 0)
  get_user = request.get_cookie("user", secret="my-secret")
  if get_user:
      user = get_user[0]
  else:
    user = None
    response.set_header("Location", "/logout")
  return template("index", title="Twitter", user=user, fake_tweets=fake_tweets, trends=trends, follows=follows, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)


##############################

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=5000, debug=True, reloader=True)