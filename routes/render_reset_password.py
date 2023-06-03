from bottle import get, template, response
import jwt
import x

SECRET_KEY = "5e28e54695db4d92980be20ea198c6a0"

@get ("/reset-password/<token>")
def _(token):
    try:
        # Decoding the token and storing the secret
        print("check 1", token)
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_email = decoded_token['user_email']
        print(user_email)

        # Check database for user
        db = x.db()
        result = db.execute("SELECT * FROM users WHERE user_email=?", (user_email,)).fetchone()
        
        # Validate if email exits 
        if result:
            print("user exists")
        else:
            print("use dont exists")
            response.status = 400
            raise Exception("User not found")

        return template('reset_password', token=token, user_email=user_email)
    except Exception as e:
        print(e)
        response.status = 303
        response.set_header("Location", "/login")
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass


# redirect to login page if user tries to go to login page
@get ("/reset-password")
def _():
    response.status = 303
    response.set_header("Location", "/login")
    return