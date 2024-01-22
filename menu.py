from PyQt6.QtWidgets import QApplication,QPushButton,QWidget,QLineEdit
import sys
import face_signup as up
import face_signin as signin

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('顔認証システム')
        #self.setGeometry(0,0,600,800)#ウィンドウの位置と大きさ
        self.initUi()

    def initUi(self):
        self.label = QLineEdit(self)
        self.label.move(100,50)
        self.button = QPushButton("登録",self)
        self.button1 = QPushButton('出席',self)
        self.button.move(100,10)
        self.button1.move(200,10)
        self.button.clicked.connect(self.toroku)
        self.button1.clicked.connect(self.syusseki)
    def toroku(self):
        self.w = up.Main()
        self.w.show()
    def syusseki(self):
        self.w = signin.main()
        self.label.setText(self.w)#printをreturnに
        #self.w.show()

        #ここから下は変更NG
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Menu()
    window.show()
    App.exec()
