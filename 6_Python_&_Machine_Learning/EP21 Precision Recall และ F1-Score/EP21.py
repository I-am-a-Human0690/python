'''
สรุป Machine Learning(EP.4)- ตัวจำแนกแบบไบรารี่ (Binary Classifier)
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-4-%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%88%E0%B8%B3%E0%B9%81%E0%B8%99%E0%B8%81%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B9%84%E0%B8%9A%E0%B8%A3%E0%B8%B2%E0%B8%A3%E0%B8%B5%E0%B9%88-binary-classifier-6ebc8e1a5e61
'''
'''
Confusion Matrix เครื่องมือสำคัญในการประเมินผลลัพธ์ของการทำนาย ในMachine learning
https://medium.com/@pagongatchalee/confusion-matrix-%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%99%E0%B8%9C%E0%B8%A5%E0%B8%A5%E0%B8%B1%E0%B8%9E%E0%B8%98%E0%B9%8C%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B8%B2%E0%B8%A2-%E0%B9%83%E0%B8%99machine-learning-fba6e3f9508c
'''
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier#คำนวนข้อมูลแค่บางส่วน (Stochastic Gradient Descent Algorithm)
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
import itertools
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

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

#EP19
# score = cross_val_score(sgd_clf,x_train,y_train_5,cv=3,scoring="accuracy") # cv = Cross-validation = จำนวนการทดลอง
# print(score)

y_train_pred = cross_val_predict(sgd_clf,x_train,y_test_5,cv=3)# cv = Cross-validation = จำนวนการทดลอง
cm=confusion_matrix(y_train_5,y_train_pred)
print(cm)

'''
print(cm) ตามรูป
#แนวกลุ่มข้อมูลค่าจริง
#แนวตั้งผลลัพที่เกิดจากการพยากรค่า
47432 7147
  898 4523

กลุ่มตัวเลขที่ไม่ใช่เลข 5 พยากรถูก 47432
และอาจมีการคาดเคลื่อนไปเป็นกลุ่มเลข 5 อยู่ 7147
กลุ่มที่อยู่ในตัวเลข 5 พยากรว่าอยู่ในกลุ่มตัวเลข 5 4523
และอาจะคาดเคลื่อนไปอยู่กลุ่มอื่น 898
'''
#แสดงเป็นแผนภาพ ConfusionMatrix
def displayConfusionMatrix(cm,cmap=plt.cm.GnBu):#cmap=plt.cm.GnBu สี
    classes=["Other Number","Number 5"]
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title("Confusion Matrix")
    plt.colorbar()
    trick_marks=np.arange(len(classes))
    plt.xticks(trick_marks,classes)
    plt.yticks(trick_marks,classes)
    thresh=cm.max()/2
    for i , j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],'d'),
        horizontalalignment='center',
        color='white' if cm[i,j]>thresh else 'black')

    plt.tight_layout()
    plt.ylabel('Actually')
    plt.xlabel('Prediction')
    plt.show()

plt.figure()
displayConfusionMatrix(cm)

y_test_pred=sgd_clf.predict(x_test)
classes=['Other Number','Number 5']
print(classification_report(y_test_5,y_test_pred,tret_names=classes))
#Precision = ความแม่นยำ
#Recall = ความถูกต้องของการทำนายว่าจะเป็น “จริง” เทียบกับ จำนวนครั้งของเหตุการณ์ทั้งทำนาย และ เกิดขึ้น ว่า “เป็นจริง” 
#แบบเป็น %
print("Accuracy Score = ",accuracy_score(y_test_5,y_test_pred)*100)