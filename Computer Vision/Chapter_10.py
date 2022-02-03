# Converting our webcam into gray and binary 
# importing a library
import cv2 as cv
import numpy as np 
# Step 2: capturing a webcam  
cap = cv.VideoCapture(0)
# Display the cam frame by  frame 
while(True): 
    (ret, frame)= cap.read()
    # making the display gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # # Changing the gray frame threshold/making it balck and white  
    (thresh ,binary ) = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
# Showing both displays 
    cv.imshow("gray_video", gray)
    cv.imshow("orignal", frame)
    cv.imshow("back&white", binary)
    # to quit the loop with q key 
    if cv.waitKey(1) & 0xFF== ord("q"):
            break
# Release /close windows easily 
cap.release()
cv.destroyAllWindows()