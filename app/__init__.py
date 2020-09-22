from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__, static_folder="static")

app.config['MYSQL_HOST']    = 'bbl.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER']    = 'bbl'
app.config['MYSQL_PASSWORD']= 'marzer1279bbl'
app.config['MYSQL_DB']      = 'bbl$chery'

mysql = MySQL(app)

from app import routes

