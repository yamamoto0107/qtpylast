"""
國本

大規模python開発に挑戦！
要件定義
・データベース(sql):attendテーブル、recordテーブル、holidayテーブル
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
from PyQt6.QtWidgets import QApplication,QWidget
import sys
from tkinter import Tk
import sqlite3
import datetime
from PyQt6.QtWidgets import QPushButton
import cv2
import face_recognition
import numpy as np
import pickle
import face_re as ft

root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.setGeometry(0,0,monitor_width,monitor_height) # ウィンドウの位置と大きさ
        self.initUi()
    
    def initUi(self):#UI関係の表示設定
        self.button = QPushButton('出席登録', self)
        self.button.clicked.connect(self.faceWindow)

#顔認識開始
class faceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('出席登録', self)
        self.button.clicked.connect(self.cam)
    
    name_test = "test"

    def cam(test):
        cap = cv2.VideoCapture(0)
        cas = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        while True:
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face = cas.detectMultiScale(gray)
            if np.all(face != None):
                cv2.imwrite("test.jpg",frame)
                break
            cv2.imshow("",frame)
        cap.release()
    cam(name_test)    

    img_test = ft.BGR2RGB(name_test)
    img_test,encode_test = ft.detect(img_test)

    with open('face_list.pickle','rb') as f:
        encode = pickle.load(f)
    results,face_distance = ft.recognition(encode,encode_test)
    print(results,face_distance)


#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()