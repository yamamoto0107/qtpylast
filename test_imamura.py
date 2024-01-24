from datetime import datetime, time
import sqlite3

# データベースに接続（存在しない場合は新規作成）
conn_attend = sqlite3.connect('attend.db')
conn_record = sqlite3.connect('record.db')

# カーソルの作成
cursor_attend = conn_attend.cursor()
cursor_record = conn_record.cursor()

#テーブルの作成
# cursor_record.execute('''
#     CREATE TABLE record (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         number STRING,
#         date DATE,
#         reason TEXT,
#         frame_num INTEGER,
#         late_num INTEGER
#     )
# ''')

inserts = ["22005", "國本　洸", "くにもと　ひかる","男","mail_address"]
cursor_attend.execute('INSERT INTO attend (number,name,kana,gender,mail) VALUES(?,?,?,?,?)', inserts)

conn_attend.commit()
cursor_attend.close()
cursor_record.close()