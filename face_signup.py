import face_recognition_test as ft
import pickle
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot
import numpy as np
import cv2
"""
ユーザーの顔写真登録。
名前の入力欄、カメラの表示枠、登録ボタン。
"""
class Video(QtCore.QThread):
    signal = QtCore.pyqtSignal(np.ndarray)
    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, frame = cap.read()
            self.frame = frame
            if ret:
                self.signal.emit(frame)
        cv2.imwrite("tmp.jpg", frame)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

    def cap(self):
        cv2.imwrite("tmp.jpg", self.frame)
        #print("OK")

class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gui()
        self.thread = Video()
        self.thread.signal.connect(self.update_image)
        self.thread.start()
        self.button.clicked.connect(self.closedEvent)

    def closedEvent(self,event):
        self.thread.cap()
        frame = cv2.imread("tmp.jpg")
        name = self.line.text()
        cv2.imwrite(str(name)+".jpg", frame)
        try:
            namelist = self.load('name_list.pickle')
            encode_list = self.load('face_list.pickle')
        except:
            pass

        if namelist == None:
            namelist = []
    
        if encode_list == None:
            encode_list = []

        name_list = []
        namelist.append(str(self.line.text()))
        name_list.append(str(self.line.text()))
        for i in name_list:
            img = ft.BGR2RGB(i)
            img, encode = ft.detect(img)
            encode_list.append(encode)
        self.dump('name_list.pickle',namelist)
        self.dump('face_list.pickle',encode_list)
        self.label2.setText("ユーザーが登録されました。")
        print("ユーザーが登録されました。")

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)

    def update_image(self,frame):
        qimg = QtGui.QImage(frame.tobytes(),frame.shape[1], frame.shape[0],
                            frame.strides[0], QtGui.QImage.Format.Format_BGR888)
        qpix = QtGui.QPixmap.fromImage(qimg)
        self.label.setPixmap(qpix)

    def gui(self):
        self.label = QtWidgets.QLabel(self)
        self.label1 = QtWidgets.QLabel("学籍番号を入力してください。",self)
        self.label2 = QtWidgets.QLabel("",self)
        self.line = QtWidgets.QLineEdit(self)
        self.button = QtWidgets.QPushButton('登録', self)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.line)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.button)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def load(self,pickle_name):
        try:
            with open(pickle_name, 'wb') as f:
                encode_list = pickle.load(f)
            return encode_list
        except:
            pass

    def dump(self,picle_name, encode_list):
        with open(picle_name, 'wb') as f:
            pickle.dump(encode_list, f)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    app.exec()

    

