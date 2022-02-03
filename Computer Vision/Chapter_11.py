# Writing videos from Cam

# importing a library
import cv2 as cv 
import numpy as np 
# reading the video 
cap = cv.VideoCapture(0)

# As we have to save the video which we are making 
#So firslty define
# wrting format, codec(JO kisi cheeez ko convert krta hai),video writer object and file output
# out = cv.VideoWriter("JoVideoSaveKrniUskaFileNam.avi",cv.VideoWriter_fourcc(c1,c2,c3,c4) 10, (frame_width, frame_hieght))
#Orignal video ki width or hight li pehley 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# *"MJPG" = "M", "J", "P", "G" means we can write this by adding * at start in same ""
out = cv.VideoWriter("resources/CamOut_video.mp4",cv.VideoWriter_fourcc(*"VIDX"), 10 , (frame_width, frame_height), isColor=False  )
# agr humar while loop theek chale to 
while (True):
    # video ko read kr k frame return ho  (yhe frame video ka object hai)
    (ret, frame) = cap.read()
    # Making a gray frame of the video 
    grayframe= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # agr simple video chahiey to gray b na likho simple frame likh lo 
    # Agr sirf gray me chahiey to jha jha binayry likha wha gray frame likh do 
    # # Changing the gray frame threshold/making it balck and white  
    (thresh ,binary ) = cv.threshold(grayframe, 127,255, cv.THRESH_BINARY)
    # to show the player
    # agr cap read kr lia
    if ret == True:
        # jo b show hoga usko write b krna ,jis k liey "out" define kia hum ne 
        out.write(binary)
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
out.release()
# sari windows bnd kr de phr 
cv.destroyAllWindows()