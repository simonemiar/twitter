from bottle import post, request, response
import x
import os
import shutil
import uuid
import time
import traceback
import bcrypt
from emails.send_verification_email import send_verification_email


@post("/api-signup")
def _():
    try:
        user_username = x.validate_username()
        user_email = x.validate_email()
        user_password = x.validate_password()
        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()
        salt = bcrypt.gensalt()

        user_id = str(uuid.uuid4()).replace("-","")
        user_verification_key = str(uuid.uuid4()).replace("-","")

        # get the default avatar
        default_avatar_path = "images/avatar/default_avatar.jpg"

        # Generate a unique filename for the user's avatar
        avatar_uuid = str(uuid.uuid4().hex)
        avatar_extension = os.path.splitext(default_avatar_path)[1]
        avatar_filename = avatar_uuid + avatar_extension

        # Create the new avatar path
        new_avatar_path = os.path.join('images/avatar', avatar_filename)

        # Copy the default avatar to the new path
        shutil.copy(default_avatar_path, new_avatar_path)
        # permanent_location = f"images/avatar/{avatar_filename}"

        user = {
            "user_id": str(uuid.uuid4().hex),
            "user_username": user_username,
            "user_email": user_email,
            "user_password": bcrypt.hashpw(user_password.encode("utf-8"), salt),
            # "user_password": 1234,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_created_at": int(time.time()),
            "user_total_followers": 0,
            "user_total_following": 0,
            "user_total_tweets": 0,
            "user_total_retweets": 0,
            "user_avatar": avatar_filename, 
            "user_banner": "default_banner.jpg",
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

        print("user created")
        send_verification_email(user_verification_key, user_email)
        db.commit() #without this, changes will not be saved in the database


        return {"info" : "user created", "user_id":user_id}
    except Exception as e:
        print(e)
        if 'db' in locals(): db.rollback()
        traceback.print_exc()
        response.status = 400
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass

