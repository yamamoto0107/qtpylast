import sqlite3
import re
from datetime import datetime, time

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

number = number

# frame_numの算出（何時間目か）
today = datetime.now().date() # 本日の日付を取得
frame1_start_datetime = datetime.combine(today, time(8, 0)) # 本日の日付と任意の時刻を結合
frame1_late_datetime = datetime.combine(today, time(9, 30)) 
frame1_end_datetime = datetime.combine(today, time(10, 30))
frame2_start_datetime = datetime.combine(today, time(10, 31))
frame2_late_datetime = datetime.combine(today, time(11, 10)) 
frame2_end_datetime = datetime.combine(today, time(12, 10))
frame3_start_datetime = datetime.combine(today, time(12, 11))
frame3_late_datetime = datetime.combine(today, time(13, 30)) 
frame3_end_datetime = datetime.combine(today, time(14, 30))
frame4_start_datetime = datetime.combine(today, time(14, 31))
frame4_late_datetime = datetime.combine(today, time(15, 10)) 
frame4_end_datetime = datetime.combine(today, time(16, 10))

time_now = datetime.now()

frame_num = 0
late_num = 0
if frame1_start_datetime <= time_now <= frame1_end_datetime:
    frame_num = 1
if frame1_late_datetime < time_now <= frame1_end_datetime:
    late_num = 1
if frame2_start_datetime <= time_now <= frame2_end_datetime:
    frame_num = 2
if frame2_late_datetime < time_now <= frame2_end_datetime:
    late_num = 1

# recodeに登録されているか
cursor_recode.execute('SELECT * FROM recode WHERE number={} AND frame_num={}'.format(number, frame_num))
rows = cursor_recode.fetchall()
inserts = [number, today, frame_num, late_num]

if rows == []: # 登録されていなかったら
    # recodeデータ登録
    cursor_recode.execute('INSERT INTO recode (number, date, frame_num, late_num) values(?,?,?,?)', inserts)
else:
    print(inserts, "登録済です")


conn_recode.commit()

cursor_attend.close()
cursor_recode.close()
