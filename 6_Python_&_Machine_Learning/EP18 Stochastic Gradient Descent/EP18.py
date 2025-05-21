from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier#คำนวนข้อมูลแค่บางส่วน (Stochastic Gradient Descent Algorithm)
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
predict_number = 500
y_train_0 = (y_train==0)
y_test_0 = (y_train==0)
# y_train = [true,true,........,false....,false]
print(y_train_0.shape,y_train)
print(y_test_0.shape,y_train)

def displayImage(x):#แสดงภาพ
    plt.imshow(x.reshape(28,28),
    cmap=plt.cm.binary,
    interpolation="nearest")
    plt.show()

def displaypredict(clf,actually_y,x):
    print("Actually = ",actually_y)
    print("pridiction =",clf.predict([x])[0])

sgd_clf = SGDClassifier()
sgd_clf.fit(x_train,y_train_0)
displayImage(x_test[predict_number])
displaypredict(sgd_clf,y_test_0[predict_number],x_test[predict_number])
