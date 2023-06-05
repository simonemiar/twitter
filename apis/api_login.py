from bottle import post, response, request
import time
import x
import bcrypt


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

        if not user_password == "123":
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
        # if not form_password == user_password:
        #     response.status = 400
        #     raise Exception("Password not found")
        if not update_verified_user == 1:
            response.status = 400
            raise Exception("Your user not verified, please check your email")
        print("test")
        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303 # is 303 wrong
        print("You are now logging in")

        # Update user_logged_in boolean
        db.execute("UPDATE users SET user_logged_in=? WHERE user_email=?", (1, logged_in_user)).fetchone()
        db.commit() #without this, changes will not be saved in the database


        return response.set_header("Location", "/")
    except Exception as ex:
        print(ex)
        response.status = 303
        return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
    
