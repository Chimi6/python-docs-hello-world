from flask import Flask
app = Flask(__name__)
import mysql.connector


@app.route("/")
def hello():
    


    print("ding")
    try:
        cnx = mysql.connector.connect(user='internadmin@internproject', password='Fullmetal1', host='internproject.mysql.database.azure.com', database='interns')
        print("connected")
    except Exception as e:
        print("failed to connect")
        print(e)

   # cursor = cnx.cursor()
    
    #query = ('select * from interns.interns')
   # cursor.execute(query)
   # records = cursor.fetchall()
   # cnx.close()
   return "Hello, 2!"
    
   
