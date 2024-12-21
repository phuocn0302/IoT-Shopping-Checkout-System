

# Python program to check 
# whether the camera is opened  
# or not 
  
  
#import numpy as np 
import cv2 
from datetime import datetime  
  
cap = cv2.VideoCapture(0) 
while(cap.isOpened()): 
      
    while True: 
          
        ret, img = cap.read() 
        cv2.imshow('img', img) 
        if cv2.waitKey(30) & 0xff == ord('c'): 
            cv2.imwrite('image/' + datetime.now().strftime('%M:%SD') + '.png', img)
        if cv2.waitKey(30) & 0xff == ord('q'): 
            break
              
    cap.release() 
    cv2.destroyAllWindows() 
else: 
    print("Camera Disconnected") 

