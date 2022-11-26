

import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='root', password='aarvibaby',
                              host='127.0.0.1',
                              database='sys',
                              auth_plugin='mysql_native_password')
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM products
                               ''', cnx)

df = pd.DataFrame(sql_query)
print (df)

#columns = ['id', 'first_name', 'last_name', 'email', 'gender'. 'City', 'Postal_Code', ]