from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)  # Create flask app
mysql = MySQL()  # Create instance to connect to mysql database.

"""
Database configurations
"""
app.config['MYSQL_DATABASE_USER'] = 'hope'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hope'
app.config['MYSQL_DATABASE_DB'] = 'roombooking'
app.config['MYSQL_DATABASE_HOST'] = '40.123.249.179'

mysql.init_app(app)