from bottle import get, template

@get ("/verified/<user_verification_key>")
def _(user_verification_key):
    print("verified page")
    return template('verified', title="Twitter", user_verification_key=user_verification_key)
    
