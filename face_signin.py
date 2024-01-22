import face_recognition_test as ft
import cv2
import face_recognition
import numpy as np
import pickle



def cam(test):
    cap = cv2.VideoCapture(0)
    cas = cv2.CascadeClassifier(
          cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
    while True:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = cas.detectMultiScale(gray)
        if np.all(face != None):
            cv2.imwrite(test+".jpg",frame)
            break
        cv2.imshow("",frame)
    cap.release()
    cv2.destroyAllWindows()
def load(name_pickle):
    with open(name_pickle,'rb') as f:
        encode = pickle.load(f)
        return encode
def main():
    name_test="test"
    cam(name_test)
    img_test =ft.BGR2RGB(name_test)
    img_test,encode_test = ft.detect(img_test)
    namelist=load('name_list.pickle')
    encode = load('face_list.pickle')
    results,face_distance = ft.recognition(encode,encode_test)
    for i in range(len(results)):
        if results[i]:
            #print(namelist[i],"さんで間違いありませんか？")
            return namelist[i]

if __name__ =="__main__":
    main()