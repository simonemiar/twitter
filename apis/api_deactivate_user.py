from bottle import delete, request
import x
import jwt

SECRET_KEY_DELETE = "c5d633499c044dab99e2b7f66c970ecf"

@delete('/api-deactivate-user')
def _():
    try:
        print("delete user post")
        # jwt token decoded from hidden input field
        delete_token = request.forms.get("delete_token")
        decoded_token = jwt.decode(delete_token, SECRET_KEY_DELETE, algorithms=['HS256'])
        user_email = decoded_token['user_email']
        print("token", user_email)

        db = x.db()
        db.execute("DELETE FROM users WHERE user_email=?", (user_email,)).fetchone()
        db.commit() #without this, changes will not be saved in the database

        return response.set_header("Location", "/logout")
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()