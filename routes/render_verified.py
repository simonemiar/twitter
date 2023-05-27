from bottle import get, template
import sqlite3

@get ("/verified/<user_verification_key>")
def _(user_verification_key):
    print("hey")
    return template('verified')