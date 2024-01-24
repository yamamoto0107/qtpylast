from PyQt6.QtWidgets import QApplication,QWidget
import sys
from tkinter import Tk
import sqlite3
import datetime
from PyQt6.QtWidgets import QPushButton
import face_recognition_test as ft
import jpholiday

#顔認識開始
class FaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.torokubutton = QPushButton('出席登録', self)
        self.torokubutton.clicked.connect(self.tojiro2)
    def tojiro2(self):
        now=datetime.datetime.now()
        print(jpholiday.year_holidays(now.year))
        self.close()   