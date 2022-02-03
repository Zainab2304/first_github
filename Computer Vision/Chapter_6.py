# Reading a video 
# importing a library
import cv2 as cv 
# reading the video 
cap = cv.VideoCapture("resources/vid1.mp4")

# Indicator if the video is readable 
if (cap.isOpened()==False):
    print("error in reading video")
else:
    print("All good ")

# reading anbd playing the video 
# While jb humari video open ho gai 
while(cap.isOpened()):
    # Return kre frame ko , cap read kr k 
    ret, frame = cap.read()
    # agr cap read kr lia
    if ret == True:
        #video show kre un frames k sath 
        cv.imshow("video_jo_b_nam_rakhlo", frame)
        #video me delay de 1 ka , 0 ka doge to video nhi chale gi wo pic k liey hai infinty loop 
        # or ager hum q press kre to video break kr de loop while wala 
        if cv.waitKey(1) & 0xFF== ord("q"):
            break
    # agr cap(video) ko read hi nhi kr pa rha to b break kr de loop ko 
    else:
        break
# video realse kre 
cap.release()
# sari windows bnd kr de phr 
cv.destroyAllWindows()
