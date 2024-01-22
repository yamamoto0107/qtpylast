import sys
from tkinter import Tk
from PyQt6.QtWidgets import QPushButton, QLabel,QApplication, QPushButton, QWidget, QLineEdit
import face_recognition_test as ft
import numpy as np
import face_signup as up
import face_signin as signin
import sqlite3

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


    
#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
