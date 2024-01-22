'''
import sqlite3
import re

dbname = 'recordsystem.db'
connection = sqlite3.connect(dbname)
cur = connection.cursor()

sql = "SELECT count (*) FROM record;"

cur.execute(sql)
rows = cur.fetchall()

connection.commit()
cur.close()
connection.close()


print(rows) # [(10,)]
'''

import sqlite3

conn = sqlite3.connect('recordsystem.db')
cursor = conn.cursor()

table_name = 'record'
query = f"SELECT COUNT(*) FROM {table_name}"
cursor.execute(query)
result = cursor.fetchone()
row_count = result[0]

cursor.close()
conn.close()

print(f"{row_count}")