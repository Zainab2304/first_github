# How to capture a webcam inside python 
# Step 1: IMporting libraries 
import cv2 as cv 
import numpy as np 

# Step 2: capturing a webcam  
cap= cv.VideoCapture(0) # if we write zero mean webcam no. 1, if 2 then webcam no. 1 , if you have more then one webcam

# indicator 
if cap.isOpened() == False:
    print("there is an error")
# Step 3 : display the cam frame by  frame 
# read the cam untill the end 

while (cap.isOpened()):
    # capture it frame by frame
    ret, frame = cap.read()

    if ret== True: # agr read kr rha hai to 
        # to display the frame 
        cv.imshow("Frame" , frame)
        # to quit the loop with q key 
        if cv.waitKey(1) & 0xFF== ord("q"):
            break
     # agr cap(video) ko read hi nhi kr pa rha to b break kr de loop ko 
    else:
        break

# Step 4: Release /close windows easily 
cap.release()
# sari windows bnd kr de phr 
cv.destroyAllWindows()
