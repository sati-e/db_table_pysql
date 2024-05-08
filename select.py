import mysql.connector


connection = mysql.connector.connect(
   user='root',   # your user
   password='',   # your password
   host='127.0.0.1',  # your host name
   database='db_store_2'
)


# creating cursor to execute the code
cursor = connection.cursor()




# select all columns
select_sql = '''select * from tb_product'''
cursor.execute(select_sql)


# register tuples and print
l_registers = cursor.fetchall()
print("List of tuples: ")


# print vertical
for record in l_registers:
   print(record)


# select names
select_sql_name = '''select name from tb_product'''
cursor.execute(select_sql_name)


# register tuples and print
l_registers = cursor.fetchall()
print("List of tuples: ")


# print vertical
for record in l_registers:
   print(record)


# commit changes
connection.commit()


# close connection
cursor.close()
connection.close()
print("connection closed")


# resultado do select em uma lista
