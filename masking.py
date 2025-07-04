import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

# 在blank的副本上绘制一个圆形
# 使用copy()避免修改原始blank
# 圆心：(图像宽度中心, 图像高度中心)
# 半径：100像素
# 颜色：255（白色）
# 厚度：-1（实心填充）
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# 显示圆形掩模
cv.imshow('circle',circle)

# 在blank的副本上绘制一个矩形
# 左上角坐标：(30,30)
# 右下角坐标：(370,370)
# 颜色：255（白色）
# 厚度：-1（实心填充）
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

# 创建特殊形状的掩模：圆形和矩形的交集
# 使用按位与操作：只有两个掩模都是白色的区域才会保留为白色
weird_shape = cv.bitwise_and(circle,rectangle) 
cv.imshow('weird_shape',weird_shape)

# 应用圆形掩模到原始图像
# 只显示圆形区域内的图像内容

# 掩膜是计算机视觉中一个核心概念，在OpenCV中被广泛应用。它是一种用于选择性处理图像特定区域的技术。
# 掩膜本质上是一个二值图像（通常为单通道），其像素值只有两种：
# 白色(255)：表示"感兴趣区域"（ROI, Region of Interest）
# 黑色(0)：表示"被忽略区域"

# 掩膜的作用就像一张模板，告诉OpenCV哪些像素需要处理，哪些像素需要忽略。

# 掩膜的工作原理
# 当将掩膜应用到图像处理操作时：
# 在掩膜为白色的区域：操作正常执行
# 在掩膜为黑色的区域：操作被跳过或忽略
masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',masked)

cv.waitKey(0)
cv.destroyAllWindows()