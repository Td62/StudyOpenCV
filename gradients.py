import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun', img)


# 边缘检测
# Laplacian	二阶导数	能同时检测所有方向边缘	对噪声敏感
# Sobel	一阶导数	可分别检测水平和垂直边缘	边缘较粗，需要组合
# Canny	多阶段算法	边缘细且连续，抗噪性好	参数调整较复杂

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian边缘检测

# cv.Laplacian()：使用拉普拉斯算子进行边缘检测，计算图像的二阶导数
# src：输入图像（单通道灰度图）
# ddepth：输出图像的数据类型（cv.CV_64F表示64位浮点）
lap = cv.Laplacian(gray, cv.CV_64F)

# np.absolute() 和 np.uint8()
# 取绝对值并转换为8位无符号整数(0-255范围)
# np.absolute()：取绝对值（因为拉普拉斯结果包含负值）
# np.uint8()：转换为0-255范围的8位无符号整数（适合显示）
# 注意：这两个操作是可视化拉普拉斯结果的必要步骤
lap = np.uint8(np.absolute(lap))  # 转换为可视化的图像格式
cv.imshow('laplacian', lap)

# Sobel边缘检测
# X方向梯度检测(水平边缘)
# 参数：输入图像，输出数据类型，x方向导数阶数，y方向导数阶数
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# Y方向梯度检测(垂直边缘)
# 参数同上，但检测垂直边缘
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# 合并X和Y方向的边缘检测结果
# 按位或运算合并两个结果
combined_sobel = cv.bitwise_or(sobelx, sobely)

# 显示Sobel边缘检测结果
# 仅X方向边缘
cv.imshow('sobelx', sobelx)
# 仅Y方向边缘
cv.imshow('sobely', sobely)
# 合并后的边缘
cv.imshow('combined_sobel', combined_sobel) 

# Canny边缘检测
# 参数：输入图像，低阈值，高阈值
# 二值边缘图像（非边缘为0，边缘为255）
canny = cv.Canny(gray, 150, 175)  
# 显示Canny边缘检测结果
cv.imshow('canny', canny)

# 等待键盘输入(0表示无限等待)
cv.waitKey(0)