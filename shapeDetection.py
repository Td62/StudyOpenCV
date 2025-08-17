import cv2 as cv
import numpy as np

def stackImages(scale,imgArray):
    """
    将多个图像堆叠成网格形式显示
    参数:
        scale (float): 图像缩放比例
        imgArray (list): 二维图像数组，可以是单行或多行布局
    返回值:
        ver (numpy.ndarray): 堆叠后的完整图像
    """
    rows = len(imgArray)  # 获取行数
    cols = len(imgArray[0])  # 获取列数
    rowsAvailable = isinstance(imgArray[0], list)  # 检查是否是多行布局
    
    # 获取第一个图像的尺寸作为参考
    width = imgArray[0][0].shape[1]  # 宽度
    height = imgArray[0][0].shape[0]  # 高度
    
    if rowsAvailable:  # 多行布局处理
        # 遍历所有图像
        for x in range ( 0, rows):
            for y in range(0, cols):
                # 调整图像尺寸
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    # 保持原比例缩放
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # 调整到参考图像尺寸
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # 如果是灰度图，转换为BGR格式
                if len(imgArray[x][y].shape) == 2: 
                    imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        
        # 创建空白图像作为占位符
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows  # 初始化水平堆叠列表
        for x in range(0, rows):
            # 水平堆叠一行图像
            hor[x] = np.hstack(imgArray[x])
        # 垂直堆叠所有行
        ver = np.vstack(hor)
    else:  # 单行布局处理
        for x in range(0, rows):
            # 调整图像尺寸
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            # 如果是灰度图，转换为BGR格式
            if len(imgArray[x].shape) == 2: 
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        # 水平堆叠所有图像
        hor= np.hstack(imgArray)
        ver = hor
    
    return ver  # 返回堆叠后的图像

def getContours(img):
    """
    从二值图像中提取轮廓并分析形状
    参数:
        img (numpy.ndarray): 输入的二值图像（Canny边缘检测结果）
    """
    # 查找轮廓
    # 返回值:
    #   contours: 轮廓点列表，每个轮廓是一个点的数组
    #   hierarchy: 轮廓层级信息
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    
    for cnt in contours:  # 遍历所有轮廓
        area = cv.contourArea(cnt)  # 计算轮廓面积
        print(area)  # 打印面积值
        
        # 只处理面积大于500的轮廓
        if area > 500:
            # 绘制蓝色轮廓
            cv.drawContours(imgContour,cnt,-1,(255,0,0),3)
            
            # 计算轮廓周长
            peri = cv.arcLength(cnt,True)  # True表示轮廓是闭合的
            
            # 多边形近似
            # 返回值:
            #   approx: 近似后的多边形顶点
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))  # 打印顶点数量
            
            objCor = len(approx)  # 获取顶点数量
            
            # 获取边界矩形
            # 返回值:
            #   (x,y): 矩形左上角坐标
            #   (w,h): 矩形宽高
            x,y,w,h =cv.boundingRect(approx)
            
            # 根据顶点数量判断形状
            if objCor ==3:
                objectType='Tri'  # 三角形
            elif objCor == 4:
                # 计算宽高比判断正方形/矩形
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = 'Square'  # 正方形
                else:
                    objectType = 'Retcangle'  # 矩形 (注意: 原始代码中的拼写)
            elif objCor > 4:
                objectType = 'Cricles'  # 圆形 (注意: 原始代码中的拼写)
            else:
                objectType='None'  # 未知形状
            
            # 绘制绿色边界矩形
            cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            
            # 添加形状标签文本
            cv.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

# 主程序
img = cv.imread('./shapes.png')  # 读取图像文件
imgContour = img.copy()  # 创建用于绘制轮廓的图像副本

# 图像预处理
gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # 转换为灰度图
blur = cv.GaussianBlur(gary,(7,7),1)  # 高斯模糊(核大小7x7, 标准差1)
canny = cv.Canny(blur,50,50)  # Canny边缘检测(双阈值均为50)

# 创建空白图像
blank = np.zeros(img.shape[:2],dtype='uint8')

# 处理轮廓
getContours(canny)  # 在边缘图上检测轮廓并绘制

# 创建图像堆栈
# 布局:
#   [原始图像, 灰度图像, 模糊图像]
#   [边缘图像, 轮廓图像, 空白图像]
imgStack = stackImages(0.8,([img,gary,blur],[canny,imgContour,blank]))

# 显示结果
cv.imshow('stack',imgStack)
cv.waitKey(0)  # 等待按键