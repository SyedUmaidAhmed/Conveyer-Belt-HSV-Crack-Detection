import os
import cv2
import sys
import numpy as np
from guizero import App, Picture, Text
from time import sleep

os.system('python single_image.py')




lowerBound_green=np.array([33,80,40])
upperBound_green=np.array([102,255,255])

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])



kernelOpen = np.ones((5,5))
kernelClose = np.ones((20,20))

kernelOpen1=np.ones((5,5))
kernelClose1=np.ones((20,20))


img = cv2.imread('Ahmed.png')

#convert BGR to HSV

imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# create the Mask

mask=cv2.inRange(imgHSV,lowerBound_green,upperBound_green)

mask1=cv2.inRange(imgHSV,lower_blue,upper_blue)

#morphology

maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

maskFinal=maskClose




maskOpen1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernelOpen1)
maskClose1=cv2.morphologyEx(maskOpen1,cv2.MORPH_CLOSE,kernelClose1)

maskFinal1=maskClose1


conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


res = cv2.bitwise_and(img, img, mask=mask1)


#cv2.drawContours(img,conts,-1,(255,0,0),3)

contours2,h = cv2.findContours(maskFinal1.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for contoura in contours2:
    area = cv2.contourArea(contoura)
    if(area > 300):
        x,y,w,h = cv2.boundingRect(contoura)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img, 'Crack', (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


for contour in conts:
    area1 = cv2.contourArea(contour)
    if(area1 > 800):
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        cv2.putText(img, 'Bottle', (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


cv2.imwrite('result.png',img)
app = App("Conveyor Belt Machine")
text = Text(app, text="\nBottle is Loading...", size=22)
picture = Picture(app, image='/home/pi/result.png')
text = Text(app, text="Bottle Status: Found", size=18, color= "red")
text = Text(app, text="\nBottle Size:	4.7 Inches", size=18, color ="green")
sleep(1)
app.update()

