import cv2 as cv
import numpy as np

# OpenCV使用 BGR 颜色空间（而不是常见的RGB）
# 三个通道的顺序是：

# 索引0：蓝色通道（Blue）
# 索引1：绿色通道（Green）
# 索引2：红色通道（Red）

# dtype='uint8'（0-255范围）
# np.zeros (高度, 宽度, 颜色通道)
blank = np.zeros((500,500,3),dtype='uint8')


# OpenCV使用 [y, x] 坐标顺序（先行后列）
# 图像坐标系统 (OpenCV)：
# (0,0)----------> X (宽度)
#   |
#   |
#   |
#   v
# Y (高度)

# 矩形区域：
# X: 300 到 399 (宽度100像素)
# Y: 200 到 299 (高度100像素)


# blank[250:251,0:500] = 255,0,0
# cv.imshow('Blue',blank)
# blank[:] = 0,255,0
# cv.imshow('Green',blank)
# blank[:] = 0,0,255
# cv.imshow('Red',blank)

cv.rectangle(blank,(100,251),(300,100),(0,255,0),thickness=3)
cv.imshow('rectangle',blank)

cv.waitKey(0)
cv.destroyAllWindows()
