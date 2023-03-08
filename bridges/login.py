from bottle import post, response, request
import time
import x

@post("/login")
def _():
    try:
        
        # x.validate_login()
        db = x.db()
        # user_email = request.forms.get("email")
        user_email = "a@a.dk"
        user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()
        print(user)
        if not user:
            response.status = 400
            raise Exception("User not found")
       
        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303

        return response.set_header("Location", "/")
    except Exception as ex:
        print(ex)
        response.status = 303
        return response.set_header(f"Location", "/login?error={ex}")
    finally: # This will always take place
        if "db" in locals(): db.close()
    

    # user = {
    #     "user_name":"simonemiar",
    #     "user_first_name":"Simone",
    #     "user_last_name":"Kragh-Jacobsen"
    # }

    # response.set_cookie("user", user, secret="my-secret", httponly=True)
    # response.status = 303
    # response.set_header("Location", "/")



#     @post("/login")
# def _():
#     try:
#         # x.validate_login()
#         db = x.db()
#         user_email = request.forms.get("email")
#         email = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()[0]
#         print(email)
#         if not email:
#             response.status=303
#             response.set_header("Location", "/login")
#             return
#         return response.set_header("Location", "/")
#     except Exception as ex:
#         response.status = 303
#         return response.set_header("Location", "/login")
#     finally: # This will always take place
#         if "db" in locals(): db.close()
    


        # db = x.db()
        # user_email = request.forms.get("email")
        # # user_email = "a@a.dk"
        # user = db.execute("SELECT * FROM users WHERE user_email=? COLLATE NOCASE",(user_email,)).fetchall()
        # print(user, "login")

        # if user_email == user:
        #     print("john")
        #     response.set_cookie("user", user, secret="my-secret", httponly=True)
        #     response.status = 303
        #     return response.set_header("Location", "/")
        
        # if user_email != user:
        #     print("john2")
        #     return response.set_header("Location", "/login")