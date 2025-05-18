# creating connection

import mysql.connector
myDB = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "hWsjr8+i#"
)

print(myDB)