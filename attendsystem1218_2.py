import sys
from tkinter import Tk
from PyQt6.QtWidgets import QPushButton, QLabel,QApplication, QPushButton, QWidget, QLineEdit
import face_recognition_test as ft
import numpy as np
import face_signup as up
import face_signin as signin
import sqlite3
from datetime import datetime, time

root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0,0,monitor_width,monitor_height) # ウィンドウの位置と大きさ
        self.initUi()
    
    def initUi(self):
        self.button = QPushButton('出席登録', self)
        self.button.clicked.connect(self.team1)
    
    #サンプル1(消してもOK)
    def team1(self):
        self.w1 = FaceWindow()
        self.w1.show()
        
# 顔認識
class FaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0,0,monitor_width,monitor_height) # ウィンドウの位置と大きさ
        self.initUi()
    def initUi(self):
        self.label = QLineEdit(self)
        self.label.resize(170, 30)
        self.label.move(100, 50)
        self.button = QPushButton("登録", self)
        self.button.move(100, 10)
        self.button1 = QPushButton("出席", self)
        self.button1.move(200, 10)
        self.button.clicked.connect(self.toroku)
        self.button1.clicked.connect(self.syusseki)
        self.button2 = QPushButton("終了", self)
        self.button2.move(100, 90)
        self.button2.clicked.connect(self.close)
        self.button3 = QPushButton("訂正", self)
        self.button3.move(200, 90)
        self.button3.clicked.connect(self.syusseki)
        # ↑recordを削除する処理が必要

    def toroku(self):
        self.w = up.Main()
        self.w.show()

    def syusseki(self):
        self.w = signin.main()
        self.label.setText(self.w + "さんおはようございます！")
        self.attend()

    def attend(self):
        # 学籍番号
        number = self.w

        # データベースに接続（存在しない場合は新規作成）
        conn_attend = sqlite3.connect('attend.db')
        conn_recode = sqlite3.connect('recode.db')

        # カーソルの作成
        cursor_attend = conn_attend.cursor()
        cursor_recode = conn_recode.cursor()

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
        if frame3_start_datetime <= time_now <= frame3_end_datetime:
            frame_num = 3
        if frame3_late_datetime < time_now <= frame3_end_datetime:
            late_num = 1
        if frame4_start_datetime <= time_now <= frame4_end_datetime:
            frame_num = 4
        if frame4_late_datetime < time_now <= frame4_end_datetime:
            late_num = 1

        # recodeからデータ取得
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
    
#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
