import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)

# 阈值处理
# 阈值处理作用：将灰度图转换为二值图像，用于图像分割、对象检测等

# 简单阈值 vs 自适应阈值：

# 简单阈值：全局固定阈值，适用于光照均匀的图像
# 自适应阈值：局部动态阈值，适用于光照不均的场景

# 实际应用：
# 文档扫描（文字二值化）
# 车牌识别
# 细胞图像分割
# 边缘检测预处理
gray = cv .cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# simple thresholding
# 简单阈值处理
# 参数：
# gray：输入的灰度图像（单通道）
# 125：阈值（threshold value），用于分割像素的临界值
# 255：最大值（分配给超过阈值的像素）
# cv.THRESH_BINARY：阈值处理类型（二值化）

# 返回值：
# ret：实际使用的阈值（与输入阈值相同，除非使用自适应方法）
# thresh：处理后的二值图像

# 对于图像中的每个像素：
# 如果像素值 > 125：设置为255（白色）
# 如果像素值 ≤ 125：设置为0（黑色）
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# 反二值化
threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('threshold inverse',thresh_inv)

# adaptive thresholding
# 自适应阈值处理

# 根据局部区域动态计算阈值
# 参数：
# src：输入图像（单通道）
# maxValue：满足条件的像素值（255）
# adaptiveMethod：自适应算法
# cv.ADAPTIVE_THRESH_MEAN_C：邻域均值 计算简单，速度快	对噪声敏感	光照变化平缓的图像
# cv.ADAPTIVE_THRESH_GAUSSIAN_C：高斯加权 对噪声鲁棒性好	计算量稍大	含噪声的图像，复杂光照条件
# thresholdType：阈值类型（只能选BINARY或BINARY_INV）
# blockSize：邻域大小（奇数，如11）blockSize：
# 值越大，邻域范围越大，细节越少
# 值越小，保留细节越多，但噪声更明显
# 常用值：3-21之间的奇数

# C：从均值/加权值中减去的常数（3）
# C 值：
# 正值：降低阈值，使更多像素变为前景
# 负值：提高阈值，使更多像素变为背景
# 常用范围：-5 到 10

# 返回值：自适应阈值处理后的图像

# 使用11×11的邻域窗口
# 计算每个窗口内像素的平均值
# 将阈值设为（平均值 - 3）
# 如果当前像素值大于此阈值，设为255（白色），否则设为0（黑色）
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive_thresh',adaptive_thresh)

cv.waitKey(0)