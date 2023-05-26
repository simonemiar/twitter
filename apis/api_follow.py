from bottle import post, request, response

@post("/api-follow")
def _():
    try:
        # TODO get user from cookie
        user = request.get_cookie("user", secret="my-secret")
        # TODO get user id from the user 

        # TODO Validate the followeers id 
        # TODO Connect to the database
        db = x.db()
        # TODO insert into followers table
        user_followee_id = request.forms.get("user_followee_id")
        return {"info":f"following success user with id: {user_followee_id}"}
    except Exception as e:
        print(e)
    finally:
        pass

