from bottle import post, response, request
import time
import x
import traceback

@post("/login")
def _():
    try:
        
        # x.validate_login()
        db = x.db()
        # user_email = request.forms.get("email")
        # user_password = request.forms.get("password")

        user_email = "b@b.dk"
        user_password = "123"
        user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()
        password = db.execute("SELECT * FROM users WHERE user_password=? COLLATE NOCASE",(user_password,)).fetchall()
        print(user)
        if not user:
            response.status = 400
            raise Exception("User not found")
        if not password:
            response.status = 400
            raise Exception("Password not found")
            
        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303

        return response.set_header("Location", "/")
    except Exception as ex:
        print(ex)
        response.status = 303
        return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
    
