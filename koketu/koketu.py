from PyQt6.QtWidgets import QApplication,QWidget
import sys
from tkinter import Tk
import sqlite3
import datetime
import jpholiday
from PyQt6.QtWidgets import QPushButton,QLineEdit,QLabel,QDateEdit
from PyQt6.QtCore import QDate

root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Koketu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0, 0, monitor_width, monitor_height) # ウィンドウの位置と大きさ
        self.initUiex()
    
    def initUiex(self):#UI関係の表示設定
        self.lavel_1 = QLabel('学籍番号', self)
        self.txt_number = QLineEdit('', self)
        self.lavel_2 = QLabel('日付', self)
        self.txt_day = QLineEdit('', self)
        
        self.lavel_3 = QLabel('理由', self)
        self.txt_reason = QLineEdit('', self)
        self.button = QPushButton('公欠登録', self)
        self.button.clicked.connect(self.insert)

        self.button.setGeometry(50, 140, 150, 30)
        self.txt_number.setGeometry(50, 10, 150, 30)
        self.lavel_1.setGeometry(0, 10, 150, 30)
        self.txt_day.setGeometry(50, 50, 150, 30)
        self.lavel_2.setGeometry(0, 50, 150, 30)
        self.txt_reason.setGeometry(50, 90, 150, 50)
        self.lavel_3.setGeometry(0, 90, 150, 30)

    def insert(self):
        # データベースファイルのパスを設定
        db_name = 'record.db'
        # データベースに接続
        self.con = sqlite3.connect(db_name)
        # データベースを操作するカーソルを作成
        self.cur = self.con.cursor()
        # 文を作成
        table = "record"
        sql = f"insert into {table} (number, date, reason) values (?, ?, ?)"
        self.cur.execute(sql, (self.txt_number.text(), self.txt_day.text(), self.txt_reason.text()))

        self.con.commit()
        # SQLの結果を出力

        # データベース接続を終了
        self.con.close()
