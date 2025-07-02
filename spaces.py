import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 灰度图：特征检测、简化计算
# HSV：颜色分割（如根据色相提取特定颜色）
# LAB：颜色校正、图像增强

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)

# 颜色空间转换

# BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


# 颜色空间还原

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr',lab_bgr)

#Matplotlib使用RGB格式

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()