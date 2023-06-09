from bottle import post, request, response
import x
import uuid
import traceback

@post("/api-verify-user")
def _():
    try: # SUCCESS
        token = request.forms.get("user_verification_key")
        print(token)
        if token == None:
            response.status = 400
            raise Exception ("There is no verifikation key")

        db = x.db()
        result = db.execute("SELECT * FROM users WHERE user_verification_key=?", (token,)).fetchone()

        print(result['user_verified'])
        verified_check = result['user_verified']

        if verified_check == 1:
            response.status = 400
            raise Exception ("This user is already verified")
            
        else:
            print("User is not already verified, we will now verify your user")
            newresult = db.execute("UPDATE users SET user_verified=? WHERE user_verification_key=?", (1,token)).fetchone()
            result = db.execute("SELECT * FROM users where user_verification_key=?", (token,)).fetchone()
            print("check", result)
            db.commit()
            return {"info":"user is now verified"}

    except Exception as ex: # SOMETHING IS WRONG
        if 'db' in locals(): db.rollback()
        response.status = 400
        return {"info" :str(ex)}
    finally: # This will always take place
        if "db" in locals(): db.close()