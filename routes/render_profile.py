


##############################
# profile page setup 

@get("/<user_username>")
# @view("profile")
def _(user_username):
    try:
                # get logged in user
        get_user = request.get_cookie("user", secret="my-secret")
        if get_user:
            user = get_user[0]
        else:
            user = None

        db = sqlite3.connect(os.getcwd() + "/twitter.db")
        db.row_factory = dict_factory
        user_profile = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE", (user_username,)).fetchone()

        if user_profile is None:
            print("User profile not found.")
            response.status = 400
            raise Exception("User do not exist")
            # Maybe redirect the user to a different page
        else:
            # Get the user's id
            # user_id = user_profile['user_id']
            user_id = user_profile.get('user_id')
            if user_id is not None:
                print(f"user id: {user_id}")

                # With that id, look up/get the respective tweets
                tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweet_created_at DESC LIMIT 10", (user_id,)).fetchall()
                print(tweets)

                print("visited user profile", user_profile)
                # Pass the tweets to the view and template it
                return template("profile", title="Twitter", user_profile=user_profile, user=user, trends=trends, tweets=tweets, follows=follows)
            else:
                print("User ID not found ")
                # Handle the case where the user ID is not found in the user profile
                # Return an appropriate response or redirect the user to a different page


    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
        traceback.print_exc()
        return "error"
    finally:
        if "db" in locals(): db.close()

    ##############################