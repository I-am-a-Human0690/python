'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-3-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A7%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%AB%E0%B9%8C%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%96%E0%B8%94%E0%B8%96%E0%B8%AD%E0%B8%A2%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99-linear-regression-891260e4a957
'''
'''
Loss Function คือ การคำนวน Error ว่า y_pred ที่โมเดลทำนายออกมา ต่างจาก y_test อยู่เท่าไร 
แล้วหาค่าเฉลี่ย เพื่อที่จะนำมาหา Gradient ของ Loss แล้วใช้อัลกอริทึม Gradient Descent เพื่อให้ Loss น้อยลงในการเทรนรอบถัดไป

(Loss ยิ่งค่าน้อยยิ่งดี)
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset=pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")

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

# compare true data & predict data เปรียบเทียบค่าที่ทำนายกับค่าจริง
df=pd.DataFrame({'Actually':y_test.flatten(),'predicted':y_pred.flatten()})#.flatten=แปลงจาก2มิติเป็น1มิติ

#การวัดประสิทธิภาพ
print("MAE = ",metrics.mean_absolute_error(y_test,y_pred))
print("MSE = ",metrics.mean_squared_error(y_test,y_pred))
print("RMSE = ",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#แสดงค่าความแม่นยำด้วย R-Square หากมีค่าเป็น 1 แสดงว่าแม่นยำที่สุด
print("Score = ",metrics.r2_score(y_test,y_pred))#ขอบเขตในช่วง -1 ถึง 1