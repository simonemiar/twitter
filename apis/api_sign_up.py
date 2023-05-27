from bottle import post, request, response
import x
import uuid
import time
import traceback
import bcrypt
from send_verification_email import send_verification_email


@post("/api-signup")
def _():
    try:
        user_username = x.validate_username()
        user_email = x.validate_email()
        user_password = x.validate_password()
        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()
        # x.validate_user_confirm_password() 
        salt = bcrypt.gensalt()


        user_id = str(uuid.uuid4()).replace("-","")
        user_verification_key = str(uuid.uuid4()).replace("-","")
        user = {
            "user_id": str(uuid.uuid4().hex),
            "user_username": user_username,
            "user_email": user_email,
            "user_password": bcrypt.hashpw(user_password.encode("utf-8"), salt),
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_created_at": int(time.time()),
            "user_total_followers": 0,
            "user_total_following": 0,
            "user_total_tweets": 0,
            "user_total_retweets": 0,
            "user_avatar": "default_avatar.jpg", 
            "user_banner": str(uuid.uuid4().hex),
            "user_verified": 0,
            "user_verification_key" : user_verification_key
        }
        # create placed holders for values
        values = ""
        for key in user:
            values += f":{key},"
        values = values.rstrip(",")
        print(values)

        db = x.db()
        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
        if total_rows_inserted != 1: raise Exception("Please, try again")

        db.commit() #without this, changes will not be saved in the database
        print("user created")
        send_verification_email(user_verification_key, user_email)

        return {"info" : "user created", "user_id":user_id}
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass

