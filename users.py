from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

"""
Registered users with access to the API.
For a large system, this information has to stored in a database.
"""
users = {
    # username : password
    "cookie": generate_password_hash("cookie") # Hash passwords, saving passwords in plain text is old age and Facebook stuff.
}

@auth.verify_password
def verify_password(username, password):
    """
    Check if the user credentials are registered.
    """
    if username in users and \
            check_password_hash(users.get(username), password):
        return username