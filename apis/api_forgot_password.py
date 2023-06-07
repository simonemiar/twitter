from bottle import post, request
import x
import jwt
import traceback
from emails.send_reset_password_email import send_reset_password_email

# Secret key for JWT token signing
SECRET_KEY_RESET = "5e28e54695db4d92980be20ea198c6a0"

@post("/api-forgot-password")
def _():
    try:
        user_email = x.validate_email()
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE user_email=?", (user_email,)).fetchone()
        # reset_key = str(uuid.uuid4().hex)

        # Generate JWT token
        token = jwt.encode({'user_email': user_email}, SECRET_KEY_RESET, algorithm='HS256')
        # print(type(token))
        
        if user:
            print("User found")
            send_reset_password_email(user_email, token)
            return "Reset password email sent"
        else:
            print("User not found")
            return "Email not found"

        return {"info": "email have been sent"}
    except Exception as e:
        print(e)
        traceback.print_exc()
        if 'db' in locals(): db.rollback()
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass
