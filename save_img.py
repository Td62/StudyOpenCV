import cv2 as cv
capture = cv.VideoCapture(0)
if not capture.isOpened():
    print("无法打开摄像头")
    exit()
i = 0    
while True:
    isTrue,frame= capture.read()
    if not isTrue:
        break
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
    elif key == ord('s'): 
        i += 1
        filename = f"./Faces/train/ciaojiang/{i}.jpg"
        cv.imwrite(filename,frame)
        print(f"图片已保存至: {filename}")
    cv.imshow('f',frame)    