'''
EP25 ทำนายโรคเบาหวานด้วย KNN และวัดประสิทธิภาพโมเดล
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
'''
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df=pd.read_csv("C:\\Users\\WTFTHE\Desktop\\code\Python\\6Python & Machine Learning\\diabetes.csv")
# print(df.shape)

#data
x=df.drop("Outcome",axis=1).values #.values เพื่อแปลงเป็น array
# print(x)

#outcome data ส่วนที่บอกว่าเป็นหรือไม่เป็น
y=df['Outcome'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)

# # find k to model
# k_neighbors=np.arange(1,9)

# #empty
# train_score = np.empty(len(k_neighbors))#np.empty	สร้างอาเรย์เปล่าๆ ตามขนาดที่กำหนด
# test_score = np.empty(len(k_neighbors))

# for i,k in enumerate(k_neighbors):
#     #1,2,3,4,5,6,7,8
#     knn=KNeighborsClassifier(n_neighbors=k)
#     knn.fit(x_train,y_train)
#     #วัดประสิทธิภาพ
#     train_score[i]=knn.score(x_train,y_train)
#     test_score[i]=knn.score(x_test,y_test)
#     print(test_score[i]*100)
'''
https://th.from-locals.com/python-enumerate-start/
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie
'''
# plt.title("compare k Value in Model")
# plt.plot(k_neighbors,test_score,label="Test Score")
# plt.plot(k_neighbors,train_score,label="Train Score")
# plt.legend()
# plt.xlabel("K Number")
# plt.ylabel("Score")
# plt.show()

knn=KNeighborsClassifier(n_neighbors=7)

#train
knn.fit(x_train,y_train)

#prediction
y_pred=knn.predict(x_test)

print(classification_report(y_test,y_pred))
'''
#Precision = ความแม่นยำ
#Recall = ความถูกต้องของการทำนายว่าจะเป็น “จริง” เทียบกับ จำนวนครั้งของเหตุการณ์ทั้งทำนาย และ เกิดขึ้น ว่า “เป็นจริง” 
F1-Score คือ ค่าที่แสดงประสิทธิภาพ โดยการนeค่า Precision และ Recall มาคำนวณหาค่าเฉลี่ย หรือ เรียกว่า Harmonic Mean 
ซึ่งค่าสูงๆถือว่า Model มีประสิทธิภาพดี 
support = ควรอยู่ในกลุ่มไหน
308 = 203+105
0 = ไม่ป่วย
1 = ป่วย
'''
#print(confusion_matrix(y_test,y_pred))
#แสดงแบบข้างล่างดีกว่า
print(pd.crosstab(y_test,y_pred,rownames=['Actually'],colnames=['Prediction'],margins=True))
