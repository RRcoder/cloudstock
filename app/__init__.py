from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__, static_folder="static")


app.config['MYSQL_HOST']    = 'localhost'
app.config['MYSQL_USER']    = 'root'
app.config['MYSQL_PASSWORD']= 'flash'
app.config['MYSQL_DB']      = 'bbl$chery'

mysql = MySQL(app)

from app import routes

