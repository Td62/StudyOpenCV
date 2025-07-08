import os
import cv2 as cv
import numpy as np

# 识别的人员列表
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
# 设置训练数据目录路径（使用原始字符串避免转义问题）
DIR = r'/home/td/Code/StudyOpenCV/Faces/train'

# 用于存储检测到的人脸特征（图像区域）
features = []
# 用于存储对应人脸的标签（人员索引）
labels = []
# 加载Haar级联分类器用于人脸检测
haarcascade = cv.CascadeClassifier('haarcascade_frontalface.xml')

def create_train():
     # 遍历人员列表中的每个人
    for person in people:
        # 构建当前人员的图像目录路径
        path = os.path.join(DIR,person)
        # 获取当前人员在列表中的索引作为标签
        label = people.index(person)
        
         # 遍历当前人员目录中的所有图像文件
        for img in os.listdir(path):
            # 构建完整的图像文件路径
            img_path = os.path.join(path,img)
            # 读取图像
            img_array = cv.imread(img_path)
            # 将图像转换为灰度图（人脸检测通常在灰度图上进行）
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            # 使用Haar级联分类器检测人脸
            # scaleFactor=1.1: 每次图像缩放的比例因子
            # minNeighbors=4: 每个候选矩形应该保留的邻居数量
            faces_rect = haarcascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
               
            # 遍历检测到的每个人脸
            for (x,y,w,h) in faces_rect:
            # 提取人脸区域（ROI - Region of Interest）
               faces_roi = gray[y:y+h,x:x+w]
            # 将人脸区域添加到特征列表
               features.append(faces_roi)
            # 将对应的标签添加到标签列表
               labels.append(label)


create_train()
print(f'length of the features = {len(features)}')
print(f'length of the labels = {len(labels)}')
print('training done ------------')

# 将特征和标签转换为NumPy数组
# dtype='object' 因为特征数组中包含不同大小的图像
features = np.array(features,dtype='object')
labels = np.array(labels)

# 创建LBPH人脸识别器
# LBPH(Local Binary Patterns Histograms)是一种常用的人脸识别算法
face_recogizer = cv.face.LBPHFaceRecognizer_create()

# 使用收集的特征和标签训练识别器
face_recogizer.train(features,labels)

# 保存训练好的模型
face_recogizer.save('face_trained.yml')
# 保存特征和标签数据（可选，用于后续分析或重新训练）
np.save('features.npy',features)
np.save('labels.npy',labels)

# p = []
# for i in os.listdir(DIR):
#     p.append(i)
# print(p)    

