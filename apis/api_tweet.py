from bottle import post, request, response
import x
import uuid
import time
import traceback

@post("/tweet")
def _():
  try: # SUCCESS
    get_user = request.get_cookie("user", secret="my-secret")
    logged_in_user = get_user['user_id']
    x.validate_tweet()
    db = x.db()
    
    tweet_id = str(uuid.uuid4().hex) #.hex is removing the - from the tweet_id
    tweet_user_fk = logged_in_user
    tweet_created_at = int(time.time()) #make it one
    tweet_message = request.forms.get("tweet_message")
    tweet_image = ""
    tweet_updated_at = int(time.time()) #int() make it one instead of two
    tweet_total_replies = ""
    tweet_total_likes = ""
    tweet_total_retweets = ""
    tweet_total_views = ""
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (tweet_id, tweet_user_fk, tweet_created_at, tweet_message, tweet_image, tweet_updated_at, tweet_total_replies, tweet_total_likes, tweet_total_retweets, tweet_total_views))
    db.commit() #without this, changes will not be saved in the database
    return {"info":"ok", "tweet_id":tweet_id}
  except Exception as ex: # SOMETHING IS WRONG
    if 'db' in locals(): db.rollback()
    response.status = 400
    return {"info" :str(ex)}
  finally: # This will always take place
    if "db" in locals(): db.close()