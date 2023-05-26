from bottle import post, request, response
import x
import uuid
import traceback

@post("/api-sign-up")
def _():
    try:
        user_name = x.validate_user_name()
        return "ok"
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        # if "db" in locals(): db.close()
        pass



# @post("/api-sign-up")
# def _():
#     try:
#         user_name = x.validate_user_name()
#         user_id = 1
#         user = {
#             "user_id" : user_id,
#             "user_name" : user_name 
#         }
#         values = ""
#         for key in user:
#             values = values + f":{key},"
#         values = values.rstrip(",")
#         print(values)

#         db.execute(f"INSERT INTO users VALUES({values})", user)
#         # db.execute("INSERT INTO users VALUES(?)", (user_name,))
#         return "ok"
#     except Exception as e:
#         print(e)
#         return {"info":str(e)}
#     finally:
#         # if "db" in locals(): db.close()
#         pass