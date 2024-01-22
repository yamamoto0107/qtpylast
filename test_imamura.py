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

inserts = [22001,"浅久野　大智","アサクノ ダイチ","男","meado"]
cursor_attend.execute('INSERT INTO attend (number,name,kana,gender,mail) VALUES(?,?,?,?,?)', inserts)

cursor_attend.close()
cursor_recode.close()