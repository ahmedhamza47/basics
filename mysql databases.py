import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'hamza',passwd = 'Hamz@',database = "python")

mycursor = mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)