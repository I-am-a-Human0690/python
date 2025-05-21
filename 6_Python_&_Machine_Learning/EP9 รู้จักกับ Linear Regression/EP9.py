#https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-3-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A7%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%AB%E0%B9%8C%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%96%E0%B8%94%E0%B8%96%E0%B8%AD%E0%B8%A2%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99-linear-regression-891260e4a957
'''
 การวิเคราะห์การถดถอยเชิงเส้น (Linear Regression)
 การวิเคราะห์การถดถอยเชิงเส้น เป็นการคำนวณหาความสัมพันธ์ระหว่างตัวแปร 2 ตัวแปร คือ ตัวแปรที่เราทราบค่า (Predictor :x ) และตัวแปรที่เราไม่ทราบค่า (Response:y) ซึ่งเป็นความสัมพันธ์แบบเชิงเส้น (Linear) โดยการคำนวณจากค่า x และ y ที่มีความสัมพันธ์กันจะใช้สมการของ Linear Regression คือ

y=ax+b
บางท่านอาจจะเรียกตัวแปร x , y ว่า

x= ตัวแปรอิสระ
y= ตัวแปรตาม

รูปแบบความชันและระยะตัดแกน
a = ความชันของเส้นตรง
b = ระยะตัดแกน y

แต่เพื่อความเข้าใจง่ายขอเรียกว่า

x=ตัวแปรที่ทราบค่า | ตัวประมาณการ(Predictor)
y=ตัวแปรที่เราไม่ทราบค่า |ตัวตอบสนอง (Response)
'''
#เป็นการสุ่มข้อมูลเพื่อมายกตัวอย่าง
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
print(x)
y=2*x+1 #2=a 1=b
plt.plot(x,y,'-r',label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper left")
plt.title("Graph y=2x+1")
plt.grid()
plt.show()