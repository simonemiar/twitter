from bottle import post, request
import x
import jwt
import bcrypt

# Secret key for JWT token signing
SECRET_KEY = "5e28e54695db4d92980be20ea198c6a0"

@post("/api-reset-password")
def _():
    try:
        print("reset post")
        # jwt token decoded from hidden input field
        token = request.forms.get("token")
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_email = decoded_token['user_email']
        print("token", user_email)

        # find user who match the jwt token
        db = x.db()
        result = db.execute("SELECT * FROM users WHERE user_email=?", (user_email,)).fetchone()
        user_email = result['user_email']
        user_current_password = result['user_password']
        print(user_current_password)

        # validate password
        user_password = x.validate_password()
        # user_confirm_password = x.validate_user_confirm_password()
        # print("check", user_confirm_password)

        #hash the new password
        salt = bcrypt.gensalt()
        new_user_password = bcrypt.hashpw(user_password.encode("utf-8"), salt)
        print("new", new_user_password)

        # Update the user and database with new hashed password 
        reset_password = db.execute("UPDATE users SET user_password=? WHERE user_email=?", (new_user_password, user_email)).fetchone()
        db.commit() #without this, changes will not be saved in the database

        return {"info": "password reset"}
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass