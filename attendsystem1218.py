"""
山本、チーム5
大規模python開発に挑戦！
要件定義
・データベース(sql):attendsystem.dbにattendテーブル、recordテーブル、holidayテーブル
・起動時に、「出席登録」「公欠登録」「出席率確認」「教員はこちら(学生登録・情報修正)」
　のボタンを用意する。
・どの機能もエラー対策をしておく。

・出席登録画面は、顔認証。OPENCVのカメラ画面と「○○さんおはようございます！」のlabelと終了ボタンのみ。自動で閉じはしない。
・顔認証(face_recognition_jec.py)で顔を認識してIDを返す。
・IDが返ってきたら今日1度も出席していない場合、recordテーブルに追加する。

・公欠登録は、学籍番号、日付、公欠理由を書くフォームと公欠申請ボタン。
・公欠申請ボタンが押されたらrecordテーブルに追加する。

・出席率確認は、学籍番号と年と月を入力するとその月の出席日数・欠席日数・出席率を出す。

・教員はこちら(学生登録・情報修正)のボタンを押すと、新規or上書きで学生を登録するフォーム。
・登録ボタンを押すとattendテーブルに登録される。

ファイル構成
attendsystem1218.py
attend.db
record.db
holiday.db
syuseki(フォルダ)
    ↳syusseki.py
    ↳face_recognition_jec.py
koketu(フォルダ)
    ↳koketu.py
kakunin(フォルダ)
    ↳kakunin.py
kyoshi(フォルダ)
    ↳kyoshi.py
etc(フォルダ)
    ↳自由に使えるテスト・実験用のフォルダです。    

データベース構成
1.attendテーブル
    ・id:オートインクリメント用登録番号(1~)
    ・number:学籍番号
    ・name:名前
    ・kana:ヨミガナ
    ・gender:性別
    ・mail:メールアドレス
    ・abbre:ニックネーム(呼んでほしい呼び方)
2.recordテーブル
    ・id:オートインクリメント用登録番号(1~)
    ・number:学籍番号
    ・date:日付
    ・reason:公欠理由(null可。nullの場合は出席)
    ・frame_num:コマチェック(1～4[時間目]出席)
    ・late_num:遅刻判定(1:遅刻、0:出席)
3.holidayテーブル
    ・id:オートインクリメント用登録番号(1~)
    ・year:年
    ・month:月
    ・day:日
    ・holiday:(0:夏休み,1:冬休み,2:春休み)
"""
from PyQt6.QtWidgets import QApplication,QWidget,QGridLayout,QLabel
import sys
from tkinter import Tk
import sqlite3
import datetime
from PyQt6.QtWidgets import QPushButton
import face_recognition_test as ft
import jpholiday
from PyQt6.QtGui import QFont 
root = Tk()
monitor_height = root.winfo_screenheight()-100
monitor_width = root.winfo_screenwidth()-100


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0,0,monitor_width,monitor_height) # ウィンドウの位置と大きさ
        self.initUi()
    
    def initUi(self):#UI関係の表示設定
        self.label1 = QLabel('24卒AI工学部',self)
        self.label2 = QLabel('ポータルアプリ',self)
        font = QFont()
        font.setPointSize(monitor_width/30)
        self.label1.setFont(font)
        self.label2.setFont(font)
        layout0 = QGridLayout(self)
        layout0.addWidget(self.label1,0,1)
        layout0.addWidget(self.label2,0,2)
        self.button = QPushButton('出席登録', self)
        self.button.setFont(font)
        self.button.setFixedSize(monitor_width/4,monitor_height/1.5)
        self.button.setStyleSheet('QPushButton{ color: white; background-color: red;border:10px solid gray;  }')
        self.button.clicked.connect(self.team1)
        self.button2 = QPushButton('公欠登録', self)
        self.button2.setFont(font)
        self.button2.setFixedSize(monitor_width/4,monitor_height/1.5)
        self.button2.setStyleSheet('QPushButton{ color: white; background-color: blue;border:10px solid gray;  }')
        self.button2.clicked.connect(self.team2)
        self.button3 = QPushButton('出席率確認', self)
        self.button3.setFont(font)
        self.button3.setFixedSize(monitor_width/4,monitor_height/1.5)
        self.button3.setStyleSheet('QPushButton{ color: white; background-color: green;border:10px solid gray;  }')
        self.button4 = QPushButton('教員はこちら', self)#(学生登録・情報修正)
        self.button4.setFont(font)
        self.button4.setFixedSize(monitor_width/4,monitor_height/1.5)
        self.button4.setStyleSheet('QPushButton{ color: white; background-color: black;border:10px solid gray;  }')
        self.button3.clicked.connect(self.team3)
        self.button4.clicked.connect(self.team4)
        
        layout0.addWidget(self.button,1,0)
        layout0.addWidget(self.button2,1,1)
        layout0.addWidget(self.button3,1,2)
        layout0.addWidget(self.button4,1,3)

        
        self.setLayout(layout0)
        
    
    def team1(self):
        self.w1 = FaceWindow()
        self.w1.show()

    def team2(self):
        self.w2 = KoketuWindow()
        self.w2.show()
    def team3(self):
        self.w3 = KakuninWindow()
        self.w3.show()
    def team4(self):
        self.w4 = KyoshiWindow()
        self.w4.show()
    

class KakuninWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.torokubutton = QPushButton('出席率確認', self)
        self.torokubutton.clicked.connect(self.tojiro)
    def tojiro(self):
        self.close()

class KyoshiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.torokubutton = QPushButton('教員はこちら(学生登録・情報修正)', self)
        self.torokubutton.clicked.connect(self.tojiro)
    def tojiro(self):
        self.close()

class KoketuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.torokubutton = QPushButton('公欠登録', self)
        self.torokubutton.clicked.connect(self.tojiro)
    def tojiro(self):
        self.close()

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




#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()