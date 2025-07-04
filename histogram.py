import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./ikun.jpg')
cv.imshow('kunkun',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# 创建圆形掩膜（ROI区域）
# 在blank的副本上操作，避免修改原始blank
# 圆心：(图像宽度中心, 图像高度中心)
# 半径：100像素
# 颜色：255（白色）
# 厚度：-1（实心填充）
mask = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('circle',mask)

# 应用掩膜到原始图像
# 使用按位与操作，只保留掩膜区域内的像素
# 第一个img和第二个img是相同的源图像
# mask参数指定要应用的掩膜
masked = cv.bitwise_and(img,img,mask=mask)
# 显示应用掩膜后的图像（只显示圆形区域）
cv.imshow('masked',masked)

# #Grayscale histogram

# images：输入图像（列表形式）
# channels：要分析的通道（灰度图：[0]，BGR彩色图：[0],[1],[2]）
# mask：指定分析区域（None表示全图）
# histSize：直方图区间数（bin数量）
# ranges：像素值范围（通常[0, 256]）

# gray_hist = cv.calcHist([img],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



# Colour histogram
# 计算并显示彩色直方图
# 创建新的图形窗口
plt.figure()
# 设置图形标题
plt.title('Colour histogram')
# 设置x轴标签（像素值区间）
plt.xlabel('bins')
# 设置y轴标签（像素数量）
plt.ylabel('# of pixels')

# 定义颜色通道标识（BGR顺序）
colors = ('b', 'g', 'r')  # b:蓝色, g:绿色, r:红色

# 遍历每个颜色通道（BGR顺序）
for i, col in enumerate(colors):
    # 计算当前通道的直方图
    # [img]: 输入图像（列表形式）
    # [i]: 通道索引（0=蓝色，1=绿色，2=红色）
    # mask: 使用的掩模（只计算掩模区域内的像素）
    # [256]: 直方图的bin数量（将0-255分成256个区间）
    # [0,256]: 像素值范围
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    
    # 使用对应颜色绘制直方图
    plt.plot(hist, color=col)
    
    # 设置x轴范围为0-255（像素值范围）
    plt.xlim([0, 256])

# 显示彩色直方图
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()