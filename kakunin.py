from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QGridLayout,QComboBox,QMessageBox
import sys
from tkinter import Tk
import sqlite3
import datetime
#import jpholiday
from PyQt6.QtWidgets import QPushButton
import datetime
root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JECAIportal') # ウィンドウのタイトル
        self.resize(640, 360)# ウィンドウの位置と大きさ
        self.initUi()
    
    def initUi(self):#UI関係の表示設定
        # グリッド(Grid)レイアウトの作成とメインウィンドウへの設定
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.label = QLabel("学籍番号", self)
        self.number = QLineEdit('',self, placeholderText="入力してください。")
        self.number.setMaxLength(7)
        self.label2 = QLabel("年", self)
        self.year = QLineEdit('',self, placeholderText="4桁で入力してください。")
        self.year.setMaxLength(4)
        self.label3 = QLabel("月", self)
        self.month = QComboBox()
        for s in ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']:
            self.month.addItem(s)
        self.button = QPushButton('出席率確認', self)

        # レイアウトにウィジェットを追加
        grid_layout.addWidget(self.label,0,0)
        grid_layout.addWidget(self.number,0,1)
        grid_layout.addWidget(self.label2,1,0)
        grid_layout.addWidget(self.year,1,1)
        grid_layout.addWidget(self.label3,2,0)
        grid_layout.addWidget(self.month,2,1)
        grid_layout.addWidget(self.button,3,1)

        self.button.clicked.connect(self.check_attendance)
    
    def check_attendance(self):
        if len(self.number.text()) != 7 and len(self.year.text()) != 4:
            QMessageBox.critical(self, 'Error', '学籍番号と年を入力してください。')
        elif len(self.number.text()) != 7:
            QMessageBox.critical(self, 'Error', '学籍番号を入力してください。')
        elif len(self.year.text()) != 4:
            QMessageBox.critical(self, 'Error', '年を入力してください。')
        else:
            self.w = AnotherWindow(self.number.text(), self.year.text(),self.month.currentText())
            self.w.show()

class AnotherWindow(QWidget):# 出席コマの検査59から74まで追加
    def syusseki(self):
        conn = sqlite3.connect('record.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

        # "TIMESTAMP"コンバータ関数 をそのまま ”DATETIME” にも使う
        sqlite3.dbapi2.converters['DATETIME'] = sqlite3.dbapi2.converters['TIMESTAMP']

        cursor = conn.cursor()
        query = "SELECT * FROM record WHERE number = ? AND date > ?"
        data=(self.number,datetime.datetime(int(self.year),int(self.month),1))#,datetime.datetime(int(self.year),int(self.month),31))
        print(data)
        result = cursor.execute(query,data)
        a=result.fetchall()
        a=len(a)
        conn.close()
        return a


    def __init__(self,number,year,month):
        super().__init__()
        # グリッド(Grid)レイアウトの作成とメインウィンドウへの設定
        self.number = number
        self.year =year
        listm = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        for i in range(len(listm)):
            if month == listm[i]:
                if i < 10:
                    month = "0"+str(i+1)
                else:
                    month = str(i+1)
                break

        self.month = month
        a = self.syusseki()
        print(a)
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.label1 = QLabel("出席コマ数",self)
        self.label2 = QLabel("曜日ごとの欠席コマ数", self)
        self.label3 = QLabel("合計欠席コマ数", self)
        self.label4 = QLabel("遅刻コマ数", self)
        self.label5 = QLabel("出席率", self)


        # レイアウトにウィジェットを追加
        grid_layout.addWidget(QLabel(number+' '+year+'年'+' '+month),0,0)
        grid_layout.addWidget(self.label1,1,1)
        grid_layout.addWidget(self.label2,1,2)
        grid_layout.addWidget(self.label3,1,3)
        grid_layout.addWidget(self.label4,1,4)
        grid_layout.addWidget(self.label5,1,5)
        grid_layout.addWidget(QLabel(str(a)),2,1)

    
#ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()