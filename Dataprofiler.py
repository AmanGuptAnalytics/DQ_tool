
import json
import mysql.connector
import pandas as pd
from dataprofiler import Data, Profiler
cnx = mysql.connector.connect(user='root', password='aarvibaby',
                              host='127.0.0.1',
                              database='sys',
                              auth_plugin='mysql_native_password')
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Users
                               ''', cnx)

df = pd.DataFrame(sql_query)
df.to_parquet('for_test.parquet', engine='auto')
#print (df)
data = Data("for_test.parquet") # Auto-Detect & Load: CSV, AVRO, Parquet, JSON, Text, URL

print(data.data.head(5)) # Access data directly via a compatible Pandas DataFrame

profile = Profiler(data) # Calculate Statistics, Entity Recognition, etc


readable_report = profile.report(report_options={"output_format": "compact"})


print(json.dumps(readable_report, indent=4))

#columns = ['id', 'first_name', 'last_name', 'email', 'gender'. 'City', 'Postal_Code', ]

#pdreport=pd.read_json(readable_report)
#print(pdreport)