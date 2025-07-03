import cv2 as cv
import numpy as np

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun', img)

# Averaging (平均模糊)
# 使用简单平均方法模糊图像
# 参数: (7,7) - 模糊核大小为7x7像素
# 特点: 简单快速，但会使图像整体模糊，边缘不清晰
average = cv.blur(img, (7,7))
cv.imshow('blur', average)  # 显示平均模糊结果

# Gaussian Blur (高斯模糊)
# 使用高斯分布权重进行模糊
# 参数: (7,7) - 核大小, 0 - 标准差(0表示自动计算)
# 特点: 比平均模糊更自然，保留更多边缘信息
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('GaussianBlur', gauss)  # 显示高斯模糊结果

# Median Blur (中值模糊)
# 使用邻域像素的中值代替中心像素值
# 参数: 7 - 核大小(必须是奇数)
# 特点: 有效去除椒盐噪声，同时保留边缘
median = cv.medianBlur(img, 7)
cv.imshow('medianBlur', median)  # 显示中值模糊结果

# Bilateral (双边滤波)
# 同时考虑空间距离和颜色相似性的模糊方法
# 参数: 7 - 邻域直径, 15 - 颜色空间标准差, 15 - 坐标空间标准差
# 特点: 保留边缘最完整，产生类似"磨皮"效果
bilateral = cv.bilateralFilter(img, 7, 15, 15)
cv.imshow('bilateral', bilateral)  # 显示双边滤波结果

cv.waitKey(0)
cv.destroyAllWindows()