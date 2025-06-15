import cv2 as cv
# img = cv.imread('./ikun.jpg')
# cv.imshow('ikun',img)
# cv.waitKey(0)

#reading videos
capture = cv.VideoCapture('./ikun.mp4')


while True:
    isTrue,frame= capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(30)& 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
