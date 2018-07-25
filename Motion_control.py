import cv2
from pyautogui import press
import numpy as np
from time import sleep
##from directkeys import PressKey,ReleaseKey, UP,DOWN
flag=True
flag2=False
flag3=False
flag4=True
flag5=True
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
f2=0
f1=0
f11=0
f22=0

cap=cv2.VideoCapture(0)


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


 
def midpoint(A,B,C,D):
	return ((A +(A+C)) * 0.5, (B + (B+D)) * 0.5)

while True:
    ret,img =cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if(flag4 == True):
            mask = cv2.inRange(hsv, greenLower, greenUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
            
    faces=face_cascade.detectMultiScale(gray, 1.9, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),5)
        if cnts!=[] and flag==True:
            print"Okay"
            flag2=True
            flag4=False
        if(flag==True and flag2==True):
            flag=False
            flag3=True
            f2,f1=midpoint(x,y,w,h)
            
        if(flag2==True and flag3==True):
            f22,f11=midpoint(x,y,w,h)
            
        if(f11>(f1+30) and flag3==True and flag5==True):
##                PressKey(DOWN)
##                ReleaseKey(UP)
                print"Down"
                press('down')

                flag5=False

        elif((f11+20)<f1 and flag3==True and flag5==True):
##                PressKey(UP)
##                ReleaseKey(DOWN)
                print"UP"
                press('up')
                flag5=False

                
        else:
                print"Normal"
                flag5=True
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
