import mysql.connector


connection = mysql.connector.connect(
   user='root',   # your user
   password='',   # your password
   host='127.0.0.1'  # your host name
   # database = 'database_name'
)


print("connection started")


# creating cursor to execute the code
cursor = connection.cursor()


# creating database
sql = "CREATE DATABASE if not exists db_store_2"
cursor.execute(sql)


# close connection
cursor.close()
connection.close()
print("connection closed")