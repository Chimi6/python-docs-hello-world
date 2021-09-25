from flask import Flask
app = Flask(__name__)
import mysql.connector
@app.route("/")
def hello():
   return "Hello, I am here!"
