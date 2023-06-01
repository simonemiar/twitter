from bottle import get, template
import jwt

SECRET_KEY = "5e28e54695db4d92980be20ea198c6a0"

@get ("/reset-password/<token>")
def _(token):
    print("check 1", token)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user_email = decoded_token['user_email']
    print(user_email)
    # validate if email exits 

    return template('reset_password', user_token=token, user_email=user_email)