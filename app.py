from flask import Flask
app = Flask(__name__)
import mysql.connector
@app.route("/")
def hello():
   return returnValue()


def returnValue():
   a = ["Big", "weenie",]
   flat_list = [item for sublist in a for item in sublist]
   return flat_list]
