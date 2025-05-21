#โปรแกรมคำนวณค่า BMI
#น้ำหนัก / ส่วนสูง ** 2
weight=int(input("กรุณากรอกน้ำหนักของท่าน (gk.) = "))
high=int(input("กรุณากรอกส่วนสูงของท่าน =(cm) "))/100
print(high)
bmi=weight/(high**2)
print("BMI = ",bmi)

'''
weight=input("กรุณากรอกน้ำหนักของท่าน (gk.) = ")
high=input("กรุณากรอกส่วนสูงของท่าน =(cm) ")
weight=int(weight)
high=int(high)
high/=100
bmi=weight/(high**2)
print("BMI = ",bmi)
'''

'''
weight=int(input("กรุณากรอกน้ำหนักของท่าน (gk.) = "))
high=int(input("กรุณากรอกส่วนสูงของท่าน =(cm) "))
high/=100
bmi=weight/(high**2)
print("BMI = ",bmi)
'''