# environment variable setup
import os
from dotenv import load_dotenv
load_dotenv()
pwd = os.getenv("root_pwd")

# creating connection

import mysql.connector
myDB = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = pwd,
    database = "pythonx"
)

# print(myDB)

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

# Inserting and fetching data
cur = myDB.cursor()
# cur.execute('INSERT INTO user VALUES(1526,"John","john@example.com","PRO")') 
# cur.execute('INSERT INTO user VALUES(6745,"Smith","Smith@example.com","REGULAR")') 
# myDB.commit()  # to save and get reflected in database
cur.execute("SELECT * FROM user")
result = cur.fetchall()
for i in result:
    print(i)
myDB.close() 