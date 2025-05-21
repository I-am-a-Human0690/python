from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset=load_iris()
'''
ทำนายดอกไม้ จากข้อมูลที่ส่งเข้าไป
'''
'''
sklearn.neighbors.KNeighborsClassifier
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
'''
#60 40
x_train,x_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],test_size=0.4,random_state=0)
'''
test_size=0.4 คือ test 0.4*100 = 40%
test_size คือ ขนาดอัตราส่วนของข้อมูลกลุ่ม test ต่อข้อมูลกลุ่ม train ในที่นี้เท่ากับ 0.2 คือ จะได้ข้อมูลกลุ่ม test 30 samples และข้อมูลกลุ่ม train 120 samples
random_state คือ ค่า seed ที่กำหนดการ random กลุ่มข้อมูล จะเป็นเลขจำนวนเต็ม ถ้ากำหนดเลขเดิม ผลการ split ก็เหมือนเดิม
'''
# print(x_train)
# print(y_train)

#Model
knn=KNeighborsClassifier(n_neighbors=10) #n_neighbors = K = จำนวนจุดใกล้เคียง ค่าเริ่มต้น คือ 5 จำนวนที่ต่างกันมีผลต่อความแม่นยำ

#train
knn.fit(x_train,y_train)

# print(x_test[1])
# print(y_test[1])

#prediction
#1pred=knn.predict([x_test[1]])
y_pred=knn.predict(x_test)

#Versicolor , Setosa , Virginica
# 1print ("ผลการพยากรณ์อยู่ในกลุ่มที่",pred)
# 1print("ทำนายว่าอยู่ในกลุ่มสายพันธุ์",iris_dataset['target_names'][pred])

print(classification_report(y_test,y_pred,target_names=iris_dataset['target_names']))
print(x_test.shape)
'''
#Precision = ความแม่นยำ
#Recall = ความถูกต้องของการทำนายว่าจะเป็น “จริง” เทียบกับ จำนวนครั้งของเหตุการณ์ทั้งทำนาย และ เกิดขึ้น ว่า “เป็นจริง” 
F1-Score คือ ค่าที่แสดงประสิทธิภาพ โดยการนeค่า Precision และ Recall มาคำนวณหาค่าเฉลี่ย หรือ เรียกว่า Harmonic Mean 
ซึ่งค่าสูงๆถือว่า Model มีประสิทธิภาพดี 
support = ควรอยู่ในกลุ่มไหน
60 = 16+23+21
'''
print("ความแม่นยำา = ",accuracy_score(y_test,y_pred))
print("ความแม่นยำา = ",accuracy_score(y_test,y_pred)*100)#*100 เพื่อแสดง %