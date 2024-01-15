﻿from unittest import result
import cv2
import face_recognition
import numpy as np

def camera(name):
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(name+'.jpg',frame)
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return name    



def BGR2RGB(name):
    
    img = face_recognition.load_image_file(name+".jpg")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img


def detect(img):
    try:   
        face_location = face_recognition.face_locations(img)[0]
        encode = face_recognition.face_encodings(img)[0]
        cv2.rectangle(img,(face_location[3],face_location[0]),
                      (face_location[1],face_location[2]),(0,255,0),2)
    except:
        print("顔が認識できません")
        encode = None
    return img,encode



def recognition(encode,encode_test):
    results = face_recognition.compare_faces(encode,encode_test,tolerance=0.5)
    face_distance = face_recognition.face_distance(encode,encode_test)
    return results,face_distance


def face_img(img_test,results,face_distance):
    cv2.putText(img_test,f'{results}{round(face_distance[0],2)}',
                (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('kunimoto',img)
    print("0に近いほど正解")
    cv2.imshow('kunimoto_test',img_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    name = "kunimoto"
    name_test = "kunimoto_test"
    img = BGR2RGB(name)
    camera(name_test)
    img,encode = detect(img)

    img_test = BGR2RGB(name_test)
    img_test,encode_test = detect(img_test)
    
    if np.all(encode == None) or np.all(encode_test == None):
        pass
    else:
        results,face_distance = recognition([encode],encode_test)
        print(results,face_distance)
        face_img(img_test,results,face_distance)