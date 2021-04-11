from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

"""
List of users with access to the API.
For a large system, users will have to be stored in a database.
"""
users = [
    User(1, "cookie", "cookie")
]

username_table = {u.username: u for u in users} # Get only usernames.
userid_table = {u.id: u for u in users} # Get only Id's.

def authenticate(username, password):
    user = username_table.get(username, None) # Check the given username in the list of registered users.
    if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
        return user

def identity(payload):
    user_id = payload["identity"]
    return userid_table.get(user_id, None)

