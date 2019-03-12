# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 19:26:33 2019

@author: atalk
"""

# -*- coding: utf-8 -*-

import cv2
import time
import Rpi.GPIO as GPIO

def redLight():
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    
def yellowLight():
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    time.sleep(5)
    
def greenLight():
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)

GPIO.setmode(BCM)
car_cascade_src = 'cars.xml'
twowheeler_cascade_src='two_wheeler.xml'
video_src = 'dataset/b.avi'


cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
two_wheeler_cascade = cv2.CascadeClassifier(twowheeler_cascade_src)
redcount=0
greencount=0

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.05,1)
    twoWheeler = car_cascade.detectMultiScale(gray,1.05,1)
    noOfCars=cars.shape[0]
    noOfBike=twoWheele.shape[0]
    
    totalno=noOfCars+noOfBikes
    if totalno>10:
        redcount=0
        if greencount=0:
            yellowLight()
        greenLight()
        greencount+=1
    if totalno<10:
        greencount=0
        if redcount=0:
            yellowLight()
        redlight()
        redcount+=1
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('video', img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()