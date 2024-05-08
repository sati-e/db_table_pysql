import mysql.connector


connection = mysql.connector.connect(
   user='root',   # your user
   password='',   # your password
   host='127.0.0.1',  # your host name
   database='db_store_2'
)


# creating cursor to execute the code
cursor = connection.cursor()


# creating products
# insert product name
var_1 = input("Name: ")


# insert product price
var_2 = float(input("Price: "))


# insert product expiration
var_3 = input("Expiration: ")


# creating product
insert_sql = f'''insert into tb_product
       (name, price, id, expiration) values
       ('{var_1}', '{var_2}','{id}' ,'{var_3}')
'''
cursor.execute(insert_sql)


# commit changes
connection.commit()


# close connection
cursor.close()
connection.close()
print("connection closed")
