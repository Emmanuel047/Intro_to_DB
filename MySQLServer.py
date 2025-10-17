import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
        print(f"An error occured {e}")
else:
    mycursor.close()
    mydb.close()
