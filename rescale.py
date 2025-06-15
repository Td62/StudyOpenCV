import cv2 as cv
# 不同缩放场景的推荐插值方法：
# 操作	推荐插值	说明
# 缩小	cv.INTER_AREA	避免锯齿，保持清晰度
# 放大	cv.INTER_LINEAR	平衡速度和质量
# 高质量放大	cv.INTER_CUBIC 或 cv.INTER_LANCZOS4	更慢但更平滑
# cv.resize() 是 OpenCV 中用于调整图像（或视频帧）大小的函数。它可以按照指定的尺寸或缩放因子来改变图像的尺寸
def rescaleFrame(frame,scale=0.75):
    # frame.shape：返回图像尺寸的元组 (高度, 宽度, 通道数)
    # frame.shape[0]：图像高度（行数）
    # frame.shape[1]：图像宽度（列数）
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('./ikun.mp4')


while True:
    isTrue,frame= capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('VideoResized', frame_resized)

    if cv.waitKey(30)& 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()