# Converting Color Image into black and white image 
import cv2 as cv
# loading the image 
img = cv.imread("resources/muz.jpg")
# Resizing the image 
img= cv.resize(img, (600,900))
#  COnverting into gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Changing the threshold 
(thresh ,binary ) = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
# Showing the images 
# SHOWing orignal image 
cv.imshow("Origninal", img)
# Showing gray image 
cv.imshow("gray", gray)
# Showing black and white image 
cv.imshow("binary_image", binary)
# Adding a delay 
cv.waitKey(0)
# CLose all window once wo quite the pic 
cv.destroyAllWindows()
