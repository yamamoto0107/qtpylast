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
>>>>>>> b7feece67ca2df9cc7ccac6de686858ecb5856ed

#顔認識開始
class faceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.torokubutton = QPushButton('出席登録', self)
        self.torokubutton.clicked.connect(self.tojiro2)
    def tojiro2(self):
        now=datetime.datetime.now()
        print(jpholiday.year_holidays(now.year))
        self.close()     
>>>>>>> b7feece67ca2df9cc7ccac6de686858ecb5856ed


    
#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
