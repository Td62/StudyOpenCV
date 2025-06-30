import cv2 as cv

img = cv.imread('./ikun.jpg')

# 将彩色图像转换为灰度图像
# cv.COLOR_BGR2GRAY 表示从BGR颜色空间（OpenCV默认格式）转灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ikun', img)      
cv.imshow('gray', gray)     

# 图像模糊处理（平滑）
# (7,7)是高斯核大小（必须是奇数），cv.BORDER_DEFAULT指定边界处理方式
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)     # 显示模糊后的图像

# 边缘检测（Canny算子）
# 参数：125是低阈值，175是高阈值（用于边缘连接）
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# 膨胀操作（扩大边缘区域）
# (7,7)是结构元素大小，iterations=3表示执行3次膨胀
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilating', dilated)

# 腐蚀操作（缩小边缘区域）
# 使用相同大小的结构元素，同样执行3次
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroding', eroded)

# 图像缩放
# 目标尺寸(500,500)，cv.INTER_CUBIC是三次插值方法（高质量缩放）
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)

# 图像裁剪
# [y坐标范围, x坐标范围]
cropped = img[200:400, 300:500]
cv.imshow('Cropping', cropped)

cv.waitKey(0)
cv.destroyAllWindows()