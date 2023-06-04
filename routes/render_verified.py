from bottle import get, template, request
import x

@get ("/verified/<user_verification_key>")
def _(user_verification_key):
    try:
        print("hey")
        print(user_verification_key)

        token = user_verification_key
        db = x.db()
        result = db.execute("SELECT * FROM users WHERE user_verification_key=?", (token,)).fetchone()

        print(result)
        print(result['user_verified'])
        verified_check = result['user_verified']


        if verified_check == 1:
            print("This user is already verified")
            # create a popup
            
        else:
            print("User is not already verified, we will now verify your user")
            newresult = db.execute("UPDATE users SET user_verified=? WHERE user_verification_key=?", (1,token)).fetchone()
            result = db.execute("SELECT * FROM users where user_verification_key=?", (token,)).fetchone()
            print("check", result)

        db.commit()
        return template('verified', title="Twitter")
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
        pass


