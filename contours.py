import cv2 as cv
import numpy as np

img = cv.imread('ikun.jpg')
cv.imshow('kun', img)

# 创建与原始图像相同尺寸的全黑图像
blank = np.zeros(img.shape, dtype='uint8')
# 显示空白图像
cv.imshow('blank', blank)

# 将彩色图像转换为灰度图像
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度图像
cv.imshow('gray', gray)

# 以下两行被注释掉，是可选的预处理步骤
# 高斯模糊处理，用于降噪
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# 使用Canny边缘检测算法
# 参数说明：125是低阈值，175是高阈值
canny = cv.Canny(img, 125, 175)
# 显示Canny边缘检测结果
cv.imshow('canny', canny)

# 使用阈值方法创建二值图像

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

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

# 查找图像中的轮廓
# 参数说明：
#   canny: 输入图像（Canny边缘检测结果）
#   cv.RETR_LIST: 轮廓检索模式（检索所有轮廓）
#   cv.CHAIN_APPROX_NONE: 轮廓近似方法（存储所有边界点）
# 返回值:
#   contours: 轮廓列表，每个轮廓是点的数组
#   hierarchies: 轮廓的层次结构信息
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} 个轮廓被检测到')

# 在空白图像上绘制所有轮廓
# cv.drawContours(image, contours, contourIdx, color, thickness)
# 参数说明：
# contours: 轮廓列表
# contourIdx: 要绘制的轮廓索引（-1表示所有）
# color: BGR元组，如(0, 0, 255)表示红色
# thickness: 线宽（-1表示填充轮廓）
cv.drawContours(blank, contours, -1, (0,0,255), 1)

cv.imshow('drawContours', blank)

cv.waitKey(0)
cv.destroyAllWindows()