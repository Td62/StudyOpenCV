import cv2 as cv

img = cv.imread('./group.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# 加载Haar级联分类器（人脸检测模型）
# 参数：XML文件路径（需提前下载）
# 返回值：CascadeClassifier对象
haarcascade = cv.CascadeClassifier('haarcascade_frontalface.xml')

# 执行人脸检测
# 参数：
#   gray - 输入灰度图像
#   scaleFactor=1.1 - 图像缩放比例（>1的值，越小检测越慢但更准确） 图像金字塔缩放比例	1.01-1.5 (常用1.1)
#   minNeighbors=3 - 候选矩形保留阈值（越大检测要求越高，误检越少
# 可选参数：
#   minSize - 最小检测目标尺寸 (e.g. (30,30))
#   maxSize - 最大检测目标尺寸
# 返回值：
#   包含检测结果的矩形列表，每个矩形格式为 (x, y, w, h)
#   x,y: 左上角坐标
#   w,h: 矩形宽高

faces_rect = haarcascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')
 
for (x,y,w,h) in faces_rect:
    print(f'{x,y,w,h}')
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detect',img)    

cv.waitKey(0)