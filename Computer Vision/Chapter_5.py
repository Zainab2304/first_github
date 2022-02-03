# Writing an Images 


import cv2 as cv
# loading the image 
img = cv.imread("resources/muz.jpg")
# Resizing the image 
img= cv.resize(img, (600,900))
#  COnverting into gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Changing the threshold/making it balck and white  
(thresh ,binary ) = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
# Saving a picture 
cv.imwrite("resources/muz_gray.jpg", gray)

