# Reading a video and converting ait to gray and binary 
# importing a library
import cv2 as cv 
# reading the video 
cap = cv.VideoCapture("resources/vid1.mp4")
# agr humar while loop theek chale to 
while (True):
    # video ko read kr k frame return ho  (yhe frame video ka object hai)
    (ret, frame) = cap.read()
    # Making a gray frame of the video 
    grayframe= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # Changing the gray frame threshold/making it balck and white  
    (thresh ,binary ) = cv.threshold(grayframe, 127,255, cv.THRESH_BINARY)
    # to show the player
    # agr cap read kr lia
    if ret == True:
        #video show kre un frames k sath jisko ab hum ne grayframe bol dia gray bna k  
        cv.imshow("video_jo_b_nam_rakhlo", binary)
        #video me delay de 1 ka , 0 ka doge to video nhi chale gi wo pic k liey hai infinty loop 
        # to quit the loop with q key 
        if cv.waitKey(1) & 0xFF== ord("q"):
            break
    # agr cap(video) ko read hi nhi kr pa rha to b break kr de loop ko 
    else:
        break
cap.release()
# sari windows bnd kr de phr 
cv.destroyAllWindows()