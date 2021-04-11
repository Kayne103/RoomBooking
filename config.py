from flaskext.mysql import MySQL
from flask import Flask
from users import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)  # Create flask app
mysql = MySQL()  # Create instance to connect to mysql database.

app.secret_key = "cookiesession"
jwt = JWT(app, authenticate, identity)

"""
Database configurations
"""
app.config['MYSQL_DATABASE_USER'] = 'hope'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hope'
app.config['MYSQL_DATABASE_DB'] = 'roombooking'
app.config['MYSQL_DATABASE_HOST'] = '10.0.38.138'

mysql.init_app(app)