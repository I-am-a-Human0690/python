#https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-2-%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B8%97%E0%B8%94%E0%B8%AA%E0%B8%AD%E0%B8%9A-119a16a901c8
#https://mtreerungroj.medium.com/machine-learning-supervised-learning-with-basic-scikit-learn-part1-99b8b2327c9
'''
กระบวนการ Machine Learning จะแบ่งข้อมูลสำคัญๆออกเป็น 2 ส่วน คือ

ข้อมูลชุดเรียนรู้ (Training Set) ถูกนำไปเรียนรู้ด้วยวิธีการเรียนรู้เครื่องจักรเพื่อสร้างเป็นโมเดล (Model) จะประกอบไปด้วย label / class เพื่อบอกว่าข้อมูลชุดนี้คืออะไร เช่น ชุดข้อมูลตัวเลข 0–9 , ข้อมูลสายพันธ์สุนัข เป็นต้น
ข้อมูลชุดทดสอบ (Test Set) ใช้ทดสอบโมเดลที่สร้างขึ้น หากโมเดลที่ทดสอบมีประสิทธิภาพดีจึงจะนำไปใช้งานจริง

ในกรณีที่ไม่มีการแบ่งข้อมูลเป็น 2 ส่วนสามารถเขียนโปรแกรมเพื่อแบ่งข้อมูลได้โดยแบ่งข้อมูลเป็น 75% สำหรับเรียนรู้และอีก 25% สำหรับทดสอบ
หรือแบ่งเองก็ได้
'''
from random import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset=load_iris()
#(150,4) 150 แถว 4 คอลัม คือ Sepal Sepal/length/width/Petal/length/Petal/width
#75%,25%
# x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0)
# print(x_train.shape)#112 = 150*0.75
# print(x_test.shape)#38 = 150*0.25
# print(y_train.shape)#112 = 150*0.75
# print(y_test.shape)#38 = 150*0.25
# #150
#train 75% = 112
#test 25%  = 38


#กำหนดเอง
#(150,4) 150 แถว 4 คอลัม คือ Sepal Sepal/length/width/Petal/length/Petal/width
#80%,2%
x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0,test_size=0.2)
#test_size=0.2 คือ test 0.2*100 = 20%
'''
test_size คือ ขนาดอัตราส่วนของข้อมูลกลุ่ม test ต่อข้อมูลกลุ่ม train ในที่นี้เท่ากับ 0.2 คือ จะได้ข้อมูลกลุ่ม test 30 samples และข้อมูลกลุ่ม train 120 samples
random_state คือ ค่า seed ที่กำหนดการ random กลุ่มข้อมูล จะเป็นเลขจำนวนเต็ม ถ้ากำหนดเลขเดิม ผลการ split ก็เหมือนเดิม
'''
print(x_train.shape)#120 = 150*0.80
print(x_test.shape)#30 = 150*0.20
print(y_train.shape)#120 = 150*0.80
print(y_test.shape)#30 = 150*0.20
#150
#train 80% = 120
#test 20%  = 30