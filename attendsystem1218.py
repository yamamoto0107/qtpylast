import sys
from tkinter import Tk
import sqlite3
import datetime
from PyQt6.QtWidgets import QPushButton
import face_recognition_test as ft

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
<<<<<<< HEAD
        self.button.clicked.connect(self.faceWindow)
=======
        self.button.clicked.connect()
    
    #サンプル1(消してもOK)
    def tojiro(self):
        self.w = AnotherWindow()
        self.w.show()

# 顔認識
class FaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0,0,monitor_width,monitor_height) # ウィンドウの位置と大きさ
        self.initUi()
    def initUi(self):
        self.label = QLineEdit(self)
        self.label.move(120, 50)
        self.button = QPushButton("登録", self)
        self.button.move(100, 10)
        self.button1 = QPushButton("出席", self)
        self.button1.move(200, 10)
        self.button.clicked.connect(self.toroku)
        self.button1.clicked.connect(self.syusseki)

    def toroku(self):
        self.w = up.Main()
        self.w.show()

    def syusseki(self):
        self.w = signin.main()
        self.label.setText(self.w)


    
#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
