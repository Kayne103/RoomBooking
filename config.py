from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)  # Create flask app
mysql = MySQL()  # Create instance to connect to mysql database.

"""
Database configurations
"""
app.config['MYSQL_DATABASE_USER'] = 'kayne'
app.config['MYSQL_DATABASE_PASSWORD'] = 'KillSwitch[103]'
app.config['MYSQL_DATABASE_DB'] = 'RoomBooking'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)