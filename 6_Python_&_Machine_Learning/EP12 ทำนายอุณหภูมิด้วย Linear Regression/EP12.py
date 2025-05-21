import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")

# dataset.plot(x='MinTemp',y='MaxTemp',style="o")
# plt.title('Min & Max Temp')
# plt.xlabel("MinTemp")
# plt.ylabel("MaxTemp")
# plt.show()

# print(dataset.shape) ขนาด
# print(dataset.describe) สถิติต่างๆ(Max Min...)

# train & test set
x = dataset["MinTemp"].values.reshape(-1,1) #.values=ค่าindex .reshape=แปลงจาก 1 มิติ เป็น 2(-1=แถว(ยาวลงไปจนหมดindex),1=คอลัม)
y = dataset["MaxTemp"].values.reshape(-1,1)

#80% - 20%
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
'''
test_size คือ ขนาดอัตราส่วนของข้อมูลกลุ่ม test ต่อข้อมูลกลุ่ม train ในที่นี้เท่ากับ 0.2 คือ จะได้ข้อมูลกลุ่ม test 30 samples และข้อมูลกลุ่ม train 120 samples
random_state คือ ค่า seed ที่กำหนดการ random กลุ่มข้อมูล จะเป็นเลขจำนวนเต็ม ถ้ากำหนดเลขเดิม ผลการ split ก็เหมือนเดิม
'''
#training
model=LinearRegression()
model.fit(x_train,y_train)

#test
y_pred=model.predict(x_test)

# #สร้างกราฟกระจาย
# plt.scatter(x_test,y_test)
# plt.plot(x_test,y_pred,color="red",linewidth=2)
# plt.show()

# compare true data & predict data เปรียบเทียบค่าที่ทำนายกับค่าจริง
df=pd.DataFrame({'Actually':y_test.flatten(),'predicted':y_pred.flatten()})#.flatten=แปลงจาก2มิติเป็น1มิติ
print(df.shape)
df1=df.head(20)#ขนาดจริงเยอะ ยกมาแย่ 20
df1.plot(kind="bar",figsize=(16,10))
plt.show()