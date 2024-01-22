import sqlite3
import re
from datetime import datetime

# データベースに接続（存在しない場合は新規作成）
conn_attend = sqlite3.connect('attend.db')
conn_recode = sqlite3.connect('recode.db')

# カーソルの作成
cursor_attend = conn_attend.cursor()
cursor_recode = conn_recode.cursor()


# テーブルの作成
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS recode (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         number INTEGER,
#         date STRING,
#         reason DATE,
#         frame_num INTEGER,
#         late_num INTEGER
#     )
# ''')

# データの取得
cursor_attend.execute('SELECT id FROM attend')

rows = cursor_attend.fetchall()

for row in rows: # row<'tuple'>
    id = row[0] # id<'int'>


# データ登録
#cursor.execute('INSERT INTO attend values(1, 22003, "今村　陽仁", "いまむら　はると", "男", "mail_address", "ima")')

#conn.commit()

cursor_attend.close()
cursor_recode.close()
