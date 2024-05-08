import mysql.connector


connection = mysql.connector.connect(
   user='root',   # your user
   password='',   # your password
   host='127.0.0.1',  # your host name
   database='db_store_2'
)


# creating cursor to execute the code
cursor = connection.cursor()


# creating table
table_sql = '''CREATE TABLE tb_product (
       name VARCHAR(45) NOT NULL,
       price DECIMAL NOT NULL,
       id int NOT NULL AUTO_INCREMENT,
       expiration DATE NULL,
       PRIMARY KEY (id)
       )'''


cursor.execute(table_sql)
# close connection
cursor.close()
connection.close()
print("connection closed")