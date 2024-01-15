import face_re as ft
import cv2
import face_recognition
import numpy as np
import pickle

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