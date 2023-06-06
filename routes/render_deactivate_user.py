from bottle import get, template, response
import jwt
import x

SECRET_KEY_DELETE = "c5d633499c044dab99e2b7f66c970ecf"

@get("/deactivate-user/<delete_token>")
def _(delete_token):
    try:
        # Decoding the token and storing the secret
        print("check 1", delete_token)
        decoded_token = jwt.decode(delete_token, SECRET_KEY_DELETE, algorithms=['HS256'])
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
            # create popup error

        return template('deactivate_user', delete_token=delete_token, user_email=user_email)
    except Exception as e:
        print(e)
        if 'db' in locals(): db.rollback()
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass
