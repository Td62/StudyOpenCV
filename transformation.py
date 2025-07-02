import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)

# OpenCV使用 [y, x] 坐标顺序（先行后列）
# 图像坐标系统 (OpenCV)：
# (0,0)----------> X (宽度)
#   |
#   |
#   |
#   v
# Y (高度)

# cv.warpAffine()函数：应用仿射变换
# 参数1：输入图像
# 参数2：变换矩阵
# 参数3：输出图像尺寸

# 第一行 [1, 0, x]：控制x轴变换
# 1：保持x轴原始比例
# 0：不进行y轴混合
# x：水平平移量
# 第二行 [0, 1, y]：控制y轴变换
# 0：不进行x轴混合
# 1：保持y轴原始比例
# y：垂直平移量

#     x: 水平平移量（正数向右，负数向左）
#     y: 垂直平移量（正数向下，负数向上）

# Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img,100,100)
cv.imshow('translated',translated)

# 获取旋转矩阵
# cv.getRotationMatrix2D()函数：计算旋转矩阵
# 参数1：旋转中心点（x, y）
# 参数2：旋转角度（度）
# 参数3：缩放因子（1.0表示保持原尺寸）
# Rotation

def rotate(img,degree,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,degree,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated = rotate(img,-45)
cv.imshow('rotated',rotated)


# cv.resize()函数：调整图像尺寸
# 功能：改变图像的宽度和高度
# 参数：
#   1. 输入图像
#   2. 目标尺寸（宽度, 高度）
#   3. 插值方法（指定缩放时使用的算法）
# 使用双三次插值法（高质量缩放）

#Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)

# cv.flip()函数：翻转图像
# 功能：沿水平轴、垂直轴或两个轴同时翻转图像
# 参数：
#   1. 输入图像
#   2. 翻转模式：
#       0: 垂直翻转（绕x轴）
#       1: 水平翻转（绕y轴）
#       -1: 同时水平和垂直翻转

#Flipping
flip = cv.flip(img,0)
cv.imshow('flip',flip)

# 图像裁剪：直接使用NumPy数组切片
# 功能：提取图像的感兴趣区域(ROI)
# 语法：img[y_start:y_end, x_start:x_end]
# 注意：图像坐标系中：
#   x轴（水平方向，从左到右，列索引）
#   y轴（垂直方向，从上到下，行索引）



#Cropping
cropped = img[200:400, 300:500]
cv.imshow('Cropping', cropped)

cv.waitKey(0)
cv.destroyAllWindows()