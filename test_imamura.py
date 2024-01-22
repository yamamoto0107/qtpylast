from datetime import datetime, time
import sqlite3

# データベースに接続（存在しない場合は新規作成）
conn_attend = sqlite3.connect('attend.db')
conn_recode = sqlite3.connect('recode.db')

# カーソルの作成
cursor_attend = conn_attend.cursor()
cursor_recode = conn_recode.cursor()

#テーブルの作成
# cursor_recode.execute('''
#     CREATE TABLE recode (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         number INTEGER,
#         date DATE,
#         reason TEXT,
#         frame_num INTEGER,
#         late_num INTEGER
#     )
# ''')
inserts = []
cursor_attend.execute('INSERT INTO attend (number, date, frame_num, late_num) values(?,?,?,?)', inserts)

cursor_attend.close()
cursor_recode.close()