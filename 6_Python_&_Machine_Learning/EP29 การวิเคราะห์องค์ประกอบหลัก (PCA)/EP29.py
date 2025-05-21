'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-5-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A7%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%AB%E0%B9%8C%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B9%8C%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%AD%E0%B8%9A%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81-pca-185c29aa8954
สรุป Machine Learning(EP.6)- การวิเคราะห์องค์ประกอบหลัก (PCA)
ลดขนาดข้อมูลที่ไม่จำเป็น
'''
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb#Seaborn เป็นไลบรารีที่ใช้ Matplotlib ด้านล่างเพื่อพล็อตกราฟ
from sklearn.datasets import make_blobs#คำสั่งจัดเตรียมหรือจำลอง
x,y=make_blobs(n_samples=100,n_features=10)#n_samples=100=แถว , n_features=10=คอลัม
# print(x)
# print(x.shape)
print("Before = ",x.shape)
pca=PCA(n_components=4)#กำหนด ลด features หรือ คอลัม ให้เหลือ 4  (ลดขนาด) แค่กำหนด

#pca.fit(x)
#x=pca.transform(x)#ลดขนาด
x=pca.fit_transform(x)#รวม #เรียนรู้และลดขนาด 
print("After = ",x.shape)

print(pca.n_components)
print(pca.explained_variance_ratio_)#ลดลงเลื่อยๆ
'''
PCA จะทำการสร้างตัวแปรที่เรียกว่า component โดยแต่ละ component จะไม่มีความสัมพันธ์กันเลย 
component ตัวแรกจะมีค่า variance สูงที่สุด ซึ่งจะอธิบาย ข้อมูลได้มากที่สุด และตัวถัดๆ ไปก็จะมี variance ลดลงตามลำดับ 
จำนวน component ที่เหมาะสมที่ถูกเลือกมาใช้จะครอบคลุม variance ประมาณ 80-90%
'''
df=pd.DataFrame({'var':pca.explained_variance_ratio_,'pc':['pC1','PC2','PC3','PC4']})
print(df)
sb.barplot(x='pc',y='var',data=df,color='c')
plt.show()