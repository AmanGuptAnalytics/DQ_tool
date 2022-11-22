

import mysql.connector

cnx = mysql.connector.connect(user='root', password='aarvibaby',
                              host='127.0.0.1',
                              database='sys',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor()
### 1. Completeness Check
query = """

SELECT (1- (id_chk+First_name_chk+last_name_check+email_check+gender_chk+City_check+PC_check)/all_cells)*100 as completeness FROM
(
SELECT SUM(CASE when id is null then 1 else 0 END) as id_chk,
       SUM(CASE when first_name is null then 1 else 0 END) as First_name_chk, 
       SUM(CASE when last_name is null then 1 else 0 END) as last_name_check,
       SUM(CASE when email is null then 1 else 0 END) as email_check,
       SUM(CASE when gender is null then 1 else 0 END) as gender_chk,
       SUM(CASE when City is null then 1 else 0 END) as City_check,
       SUM(CASE when Postal_Code is null then 1 else 0 END) as PC_check,
       count(*)*7 as all_cells
       from Users) as null_check
"""

cursor.execute(query)
result = cursor.fetchall()
print(result)

cnx.close()