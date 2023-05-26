from bottle import request
import sqlite3
import pathlib 
import re


##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.execute("PRAGMA foreign_keys=ON")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass



###################################
TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 10

def validate_tweet():
  error = f"message min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  if len(request.forms.tweet_message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.tweet_message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.tweet_message

###################################
EMAIL = "a@a.dk"
PASSWORD = "123"

# def validate_login():
#   error = f"user do not exists"
#   if request.forms.email == EMAIL: raise Exception(error)
#   return request.forms.email

###################################
USER_NAME_MIN = 4 
USER_NAME_MAX = 15 
USER_NAME_REGEX = "^[a-zA-Z0-9_-]{4,20}$"

def validate_username():
  print("*"*30)
  # print u"some unicode text \N{EURO SIGN}"
  # print b"some utf-8 encoded bytestring \xe2\x82\xac".decode('utf-8')
  print(request.forms.user_username)
  error = f"username has to be between {USER_NAME_MIN} to {USER_NAME_MAX} english letters or numbers from 0-9"
  user_username = request.forms.get("user_username")
  user_username = request.forms.user_username.strip()
  if len(request.forms.user_username) < USER_NAME_MIN: raise Exception(error)
  if len(request.forms.user_username) > USER_NAME_MAX: raise Exception(error)
  if not re.match(USER_NAME_REGEX, request.forms.user_username): raise Exception(error)
  return request.forms.user_username


###########
USER_FIRST_NAME_MIN_LENGTH = 2
USER_FIRST_NAME_MAX_LENGTH = 20
USER_FIRST_NAME_REGEX = "^[a-zA-Z]"

def validate_first_name():
  print("*"*30)
  error = f"first_name has to be between {USER_FIRST_NAME_MIN_LENGTH} to {USER_FIRST_NAME_MAX_LENGTH} english letters"
  user_first_name = request.forms.get("user_first_name")
  if len(request.forms.user_first_name) < USER_FIRST_NAME_MIN_LENGTH: raise Exception(error)
  if len(request.forms.user_first_name) > USER_FIRST_NAME_MAX_LENGTH: raise Exception(error)
  if not re.match(USER_FIRST_NAME_REGEX, request.forms.user_first_name): raise Exception(error)  
  print(request.forms.user_first_name)
  return request.forms.user_first_name

# ###########
USER_LAST_NAME_MIN_LENGTH = 2
USER_LAST_NAME_MAX_LENGTH = 20
USER_LAST_NAME_REGEX = "^[a-zA-Z\s]*$"

def validate_last_name():
  print("*"*30)
  error = f"last_name has to be between {USER_LAST_NAME_MIN_LENGTH} to {USER_LAST_NAME_MAX_LENGTH} english letters"
  user_last_name = request.forms.get("user_last_name")
  if len(request.forms.user_last_name) < USER_LAST_NAME_MIN_LENGTH: raise Exception(error)
  if len(request.forms.user_last_name) > USER_LAST_NAME_MAX_LENGTH: raise Exception(error)
  if not re.match(USER_LAST_NAME_REGEX, request.forms.user_last_name): raise Exception(error)  
  print(request.forms.user_last_name)
  return request.forms.user_last_name


###########
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

def validate_email():
  print("*"*30)
  error = f"An email address consists of a username, an @ sign, and a domain name"
  user_email = request.forms.get("user_email")
  if not re.match(REGEX_EMAIL, request.forms.user_email): raise Exception(error)
  print(request.forms.user_email)
  return request.forms.user_email

# ###########
USER_PASSWORD_MIN_LENGTH = 8
USER_PASSWORD_MAX_LENGTH = 50
REGEX_PASSWORD = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"

def validate_password():
  print("*"*30)
  error = f"Password has to be between {USER_PASSWORD_MIN_LENGTH} to {USER_PASSWORD_MAX_LENGTH} numbers, at least one upper case English letter, one lower case English letter and one number"
  user_password = request.forms.get("user_password")
  if len(request.forms.user_password) < USER_PASSWORD_MIN_LENGTH: raise Exception(error)
  if len(request.forms.user_password) > USER_PASSWORD_MAX_LENGTH: raise Exception(error)
  if not re.match(REGEX_PASSWORD, request.forms.user_password): raise Exception(error)  
  print(request.forms.user_password)
  return request.forms.user_password

# def validate_user_confirm_password():
# 	error = f"user_password and user_confirm_password do not match"
# 	request.forms.user_password = request.forms.user_password.strip()
# 	request.forms.user_confirm_password = request.forms.user_confirm_password.strip()
# 	if request.forms.user_confirm_password != request.forms.user_password: raise Exception(400, error)
# 	return request.forms.user_confirm_password
