from bottle import post, response, request, template
import time
import x
import bcrypt
import traceback

@post("/login")
def _():
    try:   
        x.validate_password()
        x.validate_email()
        db = x.db()
        salt = bcrypt.gensalt()

        form_email = request.forms.get("user_email")
        form_password = request.forms.get("user_password")
        print(form_email)
        print(form_password)

        user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(form_email,)).fetchone()
        print("bob", user)
        if not user:
            response.status = 400
            raise Exception ("User not found")
        
        user_email = user['user_email']
        user_password = user['user_password']

        if user_password == "MMDkodeord123":
            response.status = 400
            raise Exception("Your password are not hashed")
            # decode hashed password 

        user_password = bcrypt.checkpw(form_password.encode('utf8'), user_password)
        print(user_password)

        update_verified_user = user['user_verified']

        if not user:
            response.status = 400
            raise Exception ("User not found")
        if not user_password == True:
            response.status = 400
            raise Exception ("Password not found")
        if not update_verified_user == 1:
            response.status = 400
            raise Exception("Your user not verified, please check your email")

        response.set_cookie("user", user, secret="my-secret", httponly=True, samesite="None")
        response.status = 303

        return {"info": "You are now logging in"}
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        if 'db' in locals(): db.rollback()
        return {"info":str(ex)}
        # response.status = 303
        # return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
