# creating connection

import mysql.connector
myDB = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "xxxxxxxxx",
    database = "pythonx"
)

print(myDB)

# DATABASE INTERACTION
# myCur = myDB.cursor()
# # myCur.execute("CREATE DATABASE PYTHONX")
# # myCur.execute("DROP DATABASE employee")
# # myCur.execute("SHOW DATABASES")
# myDB.close() 

# CREATING TABLES
# cur = myDB.cursor()
# cur.execute("CREATE TABLE user(userId int PRIMARY KEY, username varchar(10), email varchar(25), userType varchar(10))") 
# myDB.close() 