from bottle import get, template, request
import sqlite3
import x

@get ("/verified/<user_verification_key>")
def _(user_verification_key):
    try:
        print("hey")
        print(user_verification_key)

        token = user_verification_key
        db = x.db()
        result = db.execute("SELECT * FROM users where user_verification_key=?", (token,)).fetchone()

        print(result)
        print(result['user_verified'])
        # logged_in_user = user[0]['user_verified']
        # if result:
        #     return f"User {token} exists in the database."
        # else:
        #     return f"User {token} does not exist in the database."

        # token = request.query.get('token')

        # # Retrieve the user from the database using the token
        # user = User.query.filter_by(verification_token=token).first()

        # if user:
        #     # Update the user's verification status
        #     user.is_verified = True
        #     db.session.commit()
        #     return "Verification successful!"
        # else:
        #     return "Invalid or expired verification token."

        # route handler retrieves the verification token from the URL
        # It then queries the database to find the user associated with that token.
        # If the user is found, their verification status is updated, and a success message is returned.
        # Otherwise, an error message indicating an invalid or expired token is returned.

        return template('verified')
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass