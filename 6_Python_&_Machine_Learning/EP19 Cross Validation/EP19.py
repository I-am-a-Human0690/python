'''
สรุป Machine Learning(EP.4)- ตัวจำแนกแบบไบรารี่ (Binary Classifier)
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-4-%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%88%E0%B8%B3%E0%B9%81%E0%B8%99%E0%B8%81%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B9%84%E0%B8%9A%E0%B8%A3%E0%B8%B2%E0%B8%A3%E0%B8%B5%E0%B9%88-binary-classifier-6ebc8e1a5e61
'''
'''
การวัดประสิทธิภาพ
Cross-validation Test การทดสอบประสิทธิภาพของโมเดลด้วยวิธี Cross-validation 
นี้จะทําการแบ่งข้อมูลออกเป็นหลายๆส่วน (k) เช่นกำหนดให้ k-fold=3 แสดงว่ามีการแบ่งข้อมูลออกเป็น 3 ส่วน 
หรือการทดลอง 3 ครั้งโดยผลลัพธ์ที่ได้จะบอก ผลการทดลองครั้งที่ 1 , 2 และ 3 ตามลำดับ
'''
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier#คำนวนข้อมูลแค่บางส่วน (Stochastic Gradient Descent Algorithm)
from sklearn.model_selection import cross_val_score

mnist_raw=loadmat("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\mnist-original.mat")
mnist={
"data":mnist_raw["data"].T,
"target":mnist_raw["label"][0]#"label"="target"
}
print(mnist["data"].shape)

x,y=mnist["data"],mnist["target"]

# training , test
#1-60000
#60001-70000
x_train, x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]
# ขนาด
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#class 0-9
#จัดกลุ่ม ที่เป็นเลข 0 กับไม่ใช้เลข 0
#ส่งตำแหน่งที่ 500 เข้าไป 500 คือ เลข 0
#ให้เครื่องตอบกลับออกมาว่าเป็นเลข 0 จริงไหม True False

#y_train_0 = [0,0,.......,9....,9]
predict_number = 5500
y_train_5 = (y_train==5)
y_test_5 = (y_train==5)
# y_train = [true,true,........,false....,false]
print(y_train_5.shape,y_train)
print(y_test_5.shape,y_train)

def displayImage(x):#แสดงภาพ
    plt.imshow(x.reshape(28,28),
    cmap=plt.cm.binary,
    interpolation="nearest")
    plt.show()

def displaypredict(clf,actually_y,x):
    print("Actually = ",actually_y)
    print("pridiction=",clf.predict([x])[0])

sgd_clf = SGDClassifier()
sgd_clf.fit(x_train,y_train_5)
displayImage(x_test[predict_number])
displaypredict(sgd_clf,y_test_5[predict_number],x_test[predict_number])

score = cross_val_score(sgd_clf,x_train,y_train_5,cv=3,scoring="accuracy") # cv = Cross-validation = จำนวนการทดลอง
print(score)