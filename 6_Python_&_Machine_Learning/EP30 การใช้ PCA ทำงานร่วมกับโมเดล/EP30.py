'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-5-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A7%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%AB%E0%B9%8C%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B9%8C%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%AD%E0%B8%9A%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81-pca-185c29aa8954
สรุป Machine Learning(EP.6)- การวิเคราะห์องค์ประกอบหลัก (PCA)
ลดขนาดข้อมูลที่ไม่จำเป็น หากข้อมูลเยอะจะช่วยให้ลดเวลาได้เยอะ
นำ EP27 มาใช้ PCA ว่าจะทำให้ดีขึ้นหรือลดลง
'''
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sb
from sklearn.decomposition import PCA

#load data
iris=sb.load_dataset('iris')
# print(iris.head)

x=iris.drop('species',axis=1) # 4
print(x)

y=iris['species']
print(y)

#pca
print("Before = ",x.shape)
pca=PCA(n_components=3)#กำหนด n_components=3 ลดให้เหลือ 3 คอลัม (ลดขนาด) แค่กำหนด
x_pca=pca.fit_transform(x)#เรียนรู้และลดขนาด
print("After = ",x.shape)

# add before , after
x['PCA1']=x_pca[:,0]
x['PCA2']=x_pca[:,1]
x['PCA3']=x_pca[:,2]
print(x)
'''
'PCA1','PCA2','PCA3' เป็นข้อมูลที่ลด จาก 4 เหลือ 3 คอลัม แล้วใสลงไปที่เดิม
'''

x_train,x_test,y_train,y_test=train_test_split(x,y)
print(x.head())

#Complete Data
x_train=x_train.loc[:,['PCA1', 'PCA2', 'PCA3']]#เอาเฉพาะช้อมูลที่ลดแล้ว ข้อมูลเก่าไม่เอา
print(x_train.head())
x_test=x_test.loc[:,['PCA1', 'PCA2', 'PCA3']]#เอาเฉพาะช้อมูลที่ลดแล้ว ข้อมูลเก่าไม่เอา
print(x_test.head())

model=GaussianNB()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

#Accuracy Score 92%
print("Accuracy = ",accuracy_score(y_test,y_pred))