from bottle import post, response, request
import time
import x

@post("/login")
def _():
    try:
        # x.validate_login()
        db = x.db()

        user_email = request.forms.get("email")
        user_password = request.forms.get("password")
        user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()
        password = db.execute("SELECT * FROM users WHERE user_password=? COLLATE NOCASE",(user_password,)).fetchall()
        logged_in_user = user[0]['user_verified']

        if not user:
            response.status = 400
            raise Exception("User not found")
        if not password:
            response.status = 400
            raise Exception("Password not found")
        if not logged_in_user == 1:
            response.status = 400
            raise Exception("Your user not verified, please check your email")

        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303 # is 303 wrong
        print("You are now logging in")

        return response.set_header("Location", "/")
    except Exception as ex:
        print(ex)
        response.status = 303
        return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
    
