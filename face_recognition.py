import cv2 as cv
import numpy as np

# 定义要识别的人员列表
# 这个列表必须与训练时使用的列表完全一致（顺序和内容）
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

# 加载Haar级联分类器用于人脸检测
# 这个XML文件包含训练好的特征，用于在图像中定位人脸
haarcascade = cv.CascadeClassifier('haarcascade_frontalface.xml')

# 加载训练时保存的特征和标签数据
# allow_pickle=True 允许加载包含Python对象的数据
features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy')

# 创建LBPH人脸识别器并加载训练好的模型
# LBPH(Local Binary Patterns Histograms)是一种常用的人脸识别算法
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# 从文件加载之前训练好的模型
face_recognizer.read('face_trained.yml')
# 读取要识别的测试图像
img = cv.imread(r'/home/td/Code/StudyOpenCV/Faces/val/ben_afflek/2.jpg')
# 人脸识别通常在灰度图上进行，因为颜色信息对于识别不是必需的
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

# 使用Haar级联分类器检测图像中的人脸
# 参数说明:
#   scaleFactor=1.1 - 每次图像缩小的比例因子（值越小检测越慢但更准确）
#   minNeighbors=4 - 每个候选矩形应该保留的邻居数量（值越高误检越少）
faces_rect = haarcascade.detectMultiScale(gray,1.1,4)

# 遍历检测到的每个人脸
for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    # 使用训练好的模型进行预测
    # 返回:
    #   label - 预测的标签索引（对应people列表中的索引）
    #   confidence - 置信度（值越低表示匹配越好）
    #   0表示完美匹配 <50通常表示良好的匹配 >80可能表示匹配不佳
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label={people[label]} with a confidence of {confidence}')
    # 在原始图像上标注识别结果
    # 参数说明:
    #   img - 要绘制的图像
    #   str(people[label]) - 要显示的文本（识别到的人名）
    #   (20,20) - 文本位置（左上角坐标）
    #   cv.FONT_HERSHEY_COMPLEX - 字体类型
    #   1.0 - 字体大小
    #   (0,255,0) - 文本颜色（绿色）
    #   thickness=2 - 文本粗细
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    # 在检测到的人脸周围绘制矩形框
    # 参数说明:
    #   (x,y) - 矩形左上角坐标
    #   (x+w,y+h) - 矩形右下角坐标
    #   (0,255,0) - 矩形颜色（绿色）
    #   thickness=2 - 矩形边框粗细
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detected face',img)
cv.waitKey(0)    