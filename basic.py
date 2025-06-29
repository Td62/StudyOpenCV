import cv2 as cv

img = cv.imread('./ikun.jpg')

#Convertiong to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('ikun',img)
cv.imshow('gray',gray)

#Blur

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascode

canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)


cv.waitKey(0)
cv.destroyAllWindows()