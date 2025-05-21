'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-9-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%94%E0%B8%88%E0%B8%B3%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%AD%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%A3-character-recognition-ae37be9836bf
สรุป Machine Learning(EP.9) — การจดจำตัวอักษร (Character Recognition)
'''
import matplotlib.pyplot as plt
from numpy import imag
from scipy.io import loadmat
import numpy as np
from sklearn.neural_network import MLPClassifier #ค่าเริ่มต้น hidden layer 100 node
from sklearn.metrics import accuracy_score

mnist_raw=loadmat("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\mnist-original.mat")
mnist={
"data" :mnist_raw["data"].T,
"target":mnist_raw["label"][0]
}
x,y=mnist["data"],mnist["target"]

#shuffle data
shuffle = np.random.permutation(70000)#สลับข้อมูล
x,y=x[shuffle],y[shuffle]
x_train,x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]
#print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)

fig,ax=plt.subplots(10,10,figsize=(8,8),#กำหนดช่องของรูปภาพ 10 แถว 10 คอลัม figsize=(8,8) ขนาดรูป 8*8
#fig=Figure(8*8) #ax=10แถว10คอลัม=100
subplot_kw={'xticks':[],'yticks':[]},#เส้นบอกเลข x,y แต่ละรูป
gridspec_kw=dict(hspace=0.1,wspace=0.1))#ระยะห่างระหว่างรูป
'''
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
matplotlib.pyplot.subplots
'''
#แสดงข้อมูล
# #display image data before training
# for i , axi in enumerate(ax.flat):#เก็บ fig,ax  i เก็บ index
#     axi.imshow(x_train[i].reshape(28,28),cmap='binary',interpolation='nearest')
'''
https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
Interpolations for imshow
สำหรับแบ็กเอนด์ Agg, ps และ pdf interpolation='none'จะใช้ได้ดีเมื่อมีการลดขนาดรูปภาพขนาดใหญ่ 
ในขณะที่interpolation='nearest'ทำงานได้ดีเมื่อขยายขนาดรูปภาพขนาดเล็ก
'''
#     axi.text(0.05,0.05,str(int(y_train[i])),transform=axi.transAxes,color="black")
#     #แสดงข้อความ 0.05,0.05=ตำแหน่ง str(int(y_train[i])=ตัวเลข 
#     #"axes"ระบบพิกัดของ Axes; (0, 0) คือด้านล่างซ้ายของแกน และ (1, 1) คือด้านบนขวาของแกน #ให้ตัวเลขอยู่ในรูป #ดูในรูป
# plt.show()

#create model
model=MLPClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print(accuracy_score(y_test,y_pred)*100)

#display image data After training & prediction
for i , axi in enumerate(ax.flat):#เก็บ fig,ax  i เก็บ index
    #display test image data
    axi.imshow(x_test[i].reshape(28,28),cmap='binary',interpolation='nearest')
    #display text true number image data
    axi.text(0.05,0.05,str(int(y_test[i])),transform=axi.transAxes,color="black")
    #แสดงข้อความ 0.05,0.05=ตำแหน่ง str(int(y_test[i])=ตัวเลข 
    #"axes"ระบบพิกัดของ Axes; (0, 0) คือด้านล่างซ้ายของแกน และ (1, 1) คือด้านบนขวาของแกน #ให้ตัวเลขอยู่ในรูป #ดูในรูป
    #display text predict number image data
    axi.text(0.75,0.05,str(int(y_pred[i])),transform=axi.transAxes,
    color="green" if y_pred[i] == y_test[i] else "red")
plt.show()