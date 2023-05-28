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


        return template('verified')
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass