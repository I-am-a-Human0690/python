'''
สรุป Machine Learning(EP.7)- การจัดกลุ่มด้วย K-Means(K-Means Clustering)
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-7-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-k-means-k-means-clustering-2423389f6c10
'''
'''
วิธีการ k เฉลี่ยโดยใช้ sklearn
https://phyblas.hinaboshi.com/20171224
'''
'''
2.การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Machine Learning Algorithms) 
เป็นการเรียนรู้ด้วยข้อมูลที่ไม่ถูกจัดประเภท หรือติดป้ายกำกับข้อมูล 
วิธีนี้เครื่องจะคาดเดาข้อมูลที่ได้รับและทำความเข้าใจถึงโครงสร้างที่ซ่อนอยู่ไม่สามารถหาผลลัพธ์ที่ถูกต้องได้ แต่จะใช้วิธี 
สำรวจข้อมูลและใช้การประมาณการว่าข้อมูลนั้นคืออะไร
'''
from sklearn.datasets import make_blobs#จำลองข้อมูล
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x,y=make_blobs(n_samples=300,centers=4,cluster_std=0.5,random_state=0)
'''
#cluster_std=0.5 ค่าเบี่ยงเบนมาตรฐาน ค่าเริ่มต้น 1.0
test_size คือ ขนาดอัตราส่วนของข้อมูลกลุ่ม test ต่อข้อมูลกลุ่ม train ในที่นี้เท่ากับ 0.2 คือ จะได้ข้อมูลกลุ่ม test 30 samples และข้อมูลกลุ่ม train 120 samples
random_state คือ ค่า seed ที่กำหนดการ random กลุ่มข้อมูล จะเป็นเลขจำนวนเต็ม ถ้ากำหนดเลขเดิม ผลการ split ก็เหมือนเดิม
'''
print(x)
print(y)
print(x[:,1])#เอาเฉพาะข้อมูล คอลัม 2
print(y.shape,x.shape)

#new point
x_new,y_new=make_blobs(n_samples=10,centers=4,cluster_std=0.5,random_state=0)#ข้อมูลตัวใหม่เพื่อโยนเข้าไปทดสอบให้จัดกลุ่มให้ข้อมูลใหม่

model=KMeans(n_clusters=4) #4 กลุ่ม n_clusters=จำนวนกระจุก  #KMeans(10) แบบนี้ก็ได้
model.fit(x)
y_pred=model.predict(x)#โยนข้อมูลเข้าไปให้แบ่งกลุ่ม สีจะสุ่ม
y_pred_new=model.predict(x_new)
centers=model.cluster_centers_#.cluster_centers_ คือตำแหน่งของจุดเซนทรอยด์ที่ได้มา จะมีขนาดเท่ากับ (จำนวนเซนทรอยด์,จำนวนมิติ)
print(centers)#Centroid แต่ละกลุ่ม Centroid=ค่ากลางหรือค่าเฉลี่ย
'''
[[ 0.95415778(0,0)  4.39985544(0,1)]
 [-1.35241261(1,0)  7.76731726(1,1)]
 [-1.57480456(2,0)  2.84532424(2,1)]
 [ 1.99469693(3,0)  0.8727049(3,1) ]]
'''

plt.scatter(x[:,0],x[:,1],c=y_pred) #แกน x,y #c=y_pred เอาสีตาม y_pred 
plt.scatter(x_new[:,0],x_new[:,1],c=y_pred_new,s=120) #s=size
plt.scatter(centers[0,0],centers[0,1],c='blue',label='Centroid 1' )#Centroid กลุ่ม 1
plt.scatter(centers[1,0],centers[1,1],c='green',label='Centroid 2' )#Centroid กลุ่ม 2
plt.scatter(centers[2,0],centers[2,1],c='red',label='Centroid 3' )#Centroid กลุ่ม 3
plt.scatter(centers[3,0],centers[0,1],c='black',label='Centroid 3' )#Centroid กลุ่ม 4
print(plt.legend(frameon=True))
plt.show()