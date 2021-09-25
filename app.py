from flask import Flask
app = Flask(__name__)
import mysql.connector


@app.route("/")
def hello():
    


    return "testing on"
    try:
        cnx = mysql.connector.connect(user='internadmin@internproject', password='Fullmetal1', host='internproject.mysql.database.azure.com', database='interns')
        cnx.close()
        return "connected"
    except Exception as e:
        return "failed

   # cursor = cnx.cursor()
    
    #query = ('select * from interns.interns')
   # cursor.execute(query)
   # records = cursor.fetchall()
   # cnx.close()
   return "Hello, 2!"
    
   
