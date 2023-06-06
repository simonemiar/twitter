from bottle import post, request
import jwt
import uuid
from send_deactivate_user_email import send_deactivate_user_email

SECRET_KEY_DELETE = "c5d633499c044dab99e2b7f66c970ecf"

@post ('/api-deactivate-user-email')
def _():
    try:
        print("test")
        # get cookie
        user = request.get_cookie("user", secret="my-secret")
        user_email = user[0]['user_email']
        print(user_email)
        
        # Generate JWT token
        delete_token = jwt.encode({'user_email': user_email}, SECRET_KEY_DELETE, algorithm='HS256')

        send_deactivate_user_email(user_email, delete_token)
        
        return {'info':'An email with a deactivation link has been sent to your email address.'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()