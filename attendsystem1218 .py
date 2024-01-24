from PyQt6.QtWidgets import QApplication, QWidget
import sys
from tkinter import Tk
import sqlite3
import datetime
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel
from koketu import koketu

import jpholiday

root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal')
        self.setGeometry(0, 0, monitor_width, monitor_height)
        self.initUi()

    def initUi(self):
        self.button = QPushButton('出席登録', self)
        self.button1 = QPushButton('公欠登録', self)
        self.button1.clicked.connect(self.team2)

    def team2(self):
        # 公欠登録ボタンが押されたらKoketuクラスのインスタンスを生成して表示
        self.w1 = koketu.Koketu()
        self.w1.show()


# ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
