import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)


# 颜色通道分离与合并操作
blank = np.zeros(img.shape[:2],dtype='uint8')

# 将彩色图像分离为蓝色(B)、绿色(G)、红色(R)三个独立通道
# 每个通道是单通道的灰度图像（实际存储的是该颜色分量的强度）
b,g,r = cv.split(img)

# 创建仅显示蓝色通道的图像：将蓝色通道与非空白的空白通道合并
# 相当于在蓝色通道位置保留原值，绿色和红色通道置零
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red =  cv.merge([blank,blank,r])


cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r])
cv.imshow('merge',merged)

cv.waitKey(0)
cv.destroyAllWindows()