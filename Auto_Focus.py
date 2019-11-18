import cv2 as cv
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os



def openvideo():
    capture = cv.VideoCapture(0)  
    while(True):
          ret,frame = capture.read()
          frame = cv.flip(frame,1)
          print(ret)
          gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
          lap = cv.Laplacian(gray,cv.CV_64F);
          
          x= np.var(lap);
          cv.putText(frame,str(x),(20,30),cv.FONT_ITALIC,1,(255,255,255),lineType=cv.LINE_AA)
          #Display video
          cv.imshow('video',frame)
          print(x)
                     
          key = cv.waitKey(1) &0xFF
           #To quit the tracking press 'ESC'
          if key == 27:
             break
            
    capture.release()
    cv.destroyAllWindows()

openvideo()
