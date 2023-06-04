from bottle import get, template, response

@get("/login")
def _():
    return template("login")
