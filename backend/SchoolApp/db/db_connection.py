import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school_flask'
)
my_cursor = mydb.cursor()