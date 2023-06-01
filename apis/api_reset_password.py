from bottle import post, request
import x
import jwt

# Secret key for JWT token signing
SECRET_KEY = "5e28e54695db4d92980be20ea198c6a0"

@post("/api-reset-password")
def _():
    try:
        print("reset post")
        # validate password
        # validate email
        
        # print(token)
        user_token = request.forms.get("user_token")
        decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=['HS256'])
        user_email = decoded_token['user_email']
        print(user_email)

        # user_email = request.forms.get("user_email")
        # print("check2", user_email)
        # user_token = request.forms.get("user_token")
        # print("check3", check)

        return {"info": "password reset"}
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass