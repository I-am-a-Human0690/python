#โปรแกรมคำนวณค่า BMI
#น้ำหนัก / ส่วนสูง ** 2
weight=int(input("กรุณากรอกน้ำหนักของท่าน (gk.) = "))
high=int(input("กรุณากรอกส่วนสูงของท่าน =(cm) "))/100
BMI = weight/(high**2)
#BMI=float("%.1f"%(BMI)) #แปลงเป็น 1 ตำแหน่ง
BMI=float("{:.1f}".format(BMI)) #แปลงเป็น 1 ตำแหน่ง
print(BMI)
'''
วิธีที่ 1
<18.5 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = โรคอ้วนระบบ 1
25.0 - 29.9 = โรคอ้วนระบบ 2
>30 = โรคอ้วนระบบ 3 อันตราย
'''
'''
if BMT>=18.5:
    if BMT>=18.5 and BMT<=22.9:
        print("สมส่วน")
    elif BMT>=23.0 and BMT<=24.9:
        print("โรคอ้วนระบบ 1")
    elif BMT>=25.0 and BMT<=29.9:
        print("โรคอ้วนระบบ 2")
    elif BMT>29.9:
        print("โรคอ้วนระบบ 3")
else:
    print("ต่ำกว่าเกณฑ์")
'''
#วิธีที่ดี
if BMI>=0 and BMI<=18.4:
    a="ต่ำกว่าเกณฑ์"
elif BMI>=18.5 and BMI<=22.9:
    a="สมส่วน"
elif BMI>=23.0 and BMI<=24.9:
    a="โรคอ้วนระบบ 1"
elif BMI>=25.0 and BMI<=29.9:
    a="โรคอ้วนระบบ 2"
elif BMI>29.9:
    a="โรคอ้วนระบบ 3"
else:
    a="ไม่ทราบค่าที่ชัดเจน"#กันค่าติดลบ
print("ค่า BMI = ",BMI,"ทำนายว่า ",a)


