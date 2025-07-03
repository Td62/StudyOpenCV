import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

# AND：用于提取两个图像共有的区域（如前景提取）
# OR：用于合并多个掩码或图像区域
# XOR：用于检测图像之间的差异区域
# NOT：用于反转掩码或创建反色图像

#bitwise AND
# 位运算 AND（按位与）
# 结果：只在两个图像都为白色的区域显示白色（交集）
# 1 AND 1 = 1, 其他情况 = 0
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

#bitwise OR
# 位运算 OR（按位或）
# 结果：任意一个图像为白色的区域都显示白色（并集）
# 0 OR 0 = 0, 其他情况 = 1
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

#bitwise XOR
# 位运算 XOR（按位异或）
# 结果：只在其中一个图像为白色的区域显示白色（非重叠区域）
# 相同为0，不同为1
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor',bitwise_xor)

#bitwise NOT
# 位运算 NOT（按位非）
# 结果：反转图像颜色（取反）
# 0变为255，255变为0
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not',bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()