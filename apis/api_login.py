from bottle import post, response, request, template
import time
import x
import bcrypt
import traceback

@post("/login")
def _():
    try:   
        # x.validate_password()
        db = x.db()
        salt = bcrypt.gensalt()

        user_email = request.forms.get("user_email")
        form_password = request.forms.get("user_password")
        print(form_password)

        user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()
        user_password = user[0]['user_password']
        print(user_password)

        if user_password == "MMDkodeord123":
            response.status = 400
            raise Exception("Your password are not hashed")
            # decode hashed password 

        user_password = bcrypt.checkpw(form_password.encode('utf8'), user_password)
        print(user_password)

        logged_in_user = user[0]['user_email']
        update_verified_user = user[0]['user_verified']

        if not user:
            response.status = 400
            raise Exception("User not found")
        if not user_password == True:
            response.status = 400
            raise Exception("Password not found")
        if not update_verified_user == 1:
            response.status = 400
            raise Exception("Your user not verified, please check your email")
        print("test")
        response.set_cookie("user", user, secret="my-secret", httponly=True, samesite="None")
        # response.status = 303 # is 303 wrong
        print("You are now logging in")
        response.status = 303

        return response.set_header(f"Location", "/")
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        if 'db' in locals(): db.rollback()
        response.status = 303
        return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
