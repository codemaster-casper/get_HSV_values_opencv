#!/usr/bin/python3

#importing libraries
import cv2
import numpy as np

#defining an empty function for trackbar
def empty(dummy):
    pass

#Creating a new window "HSV" and creating trackbars in it
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

#importing img, comment 'img' if you wanna use default camera feed
img = cv2.imread("Test Image.jpg")


"""
#<--If using camera, uncomment seaction A and comment section B-->

#<section A start>
#Creating an object and capturing video in it and setting dimentions
cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4,frameHeight)

while True:
    #capturing frames from the video
    success, frame = cap.read()

    #converting the RGB to HSV to read the  
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #
    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("VALUE Max","HSV")
    v_max = cv2.getTrackbarPos("VALUE Max","HSV")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask  = cv2.inRange(frameHSV,lower,upper)
    result= cv2.bitwise_and(frame,frame,mask=mask)


    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    hStack = np.hstack([frame,result,mask])

    
    cv2.imshow("hstack",hStack)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Original Video", frame)
    #cv2.imshow("Result",result)
    #cv2.imshow("HSV frame", frameHSV)

    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#<Section A End>
"""

#<Section B Start>
while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #getting the current positions of the trackbar
    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("VALUE Max","HSV")
    v_max = cv2.getTrackbarPos("VALUE Max","HSV")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask  = cv2.inRange(imgHSV,lower,upper)
    result= cv2.bitwise_and(img,img,mask=mask)

    #creating mask to detect the color
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    #hStack = np.hstack([img,result,mask])

    cv2.imshow("Original Image", img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)
    cv2.imshow("HSV Image", imgHSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#<Section B End>

cap.release()
cv2.destroyALlWindows()
