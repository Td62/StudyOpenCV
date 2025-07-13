import cv2 as cv
import numpy as np

# 定义要识别的人员列表
# 这个列表必须与训练时使用的列表完全一致（顺序和内容）
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling','ciaojiang']

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
# 大于此值视为未知
CONFIDENCE_THRESHOLD = 60  
capture = cv.VideoCapture(0)
if not capture.isOpened():
    print("无法打开摄像头")
    exit()
while True:
    isTrue,frame= capture.read()
    if not isTrue:
        break
    if cv.waitKey(30)& 0xFF==ord('q'):
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces_rect = haarcascade.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h,x:x+w]
        label,confidence = face_recognizer.predict(faces_roi)
        print(f'label={people[label]} with a confidence of {confidence}')
        # 根据置信度确定显示文本
        if confidence > CONFIDENCE_THRESHOLD:
            display_text = 'unknown'
            text_color = (0, 0, 255)
        else:
            display_text = people[label]
            text_color = (0, 255, 0)
        
        # 在图像上绘制结果
        cv.putText(frame, display_text, (x, y-30), 
                  cv.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
        cv.rectangle(frame, (x, y), (x+w, y+h), text_color, 2)
    cv.imshow('Video',frame)
capture.release()
cv.destroyAllWindows()   