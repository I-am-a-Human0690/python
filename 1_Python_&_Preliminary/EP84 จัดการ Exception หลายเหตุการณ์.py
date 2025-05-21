#Exeption
    #try
'''
try:
    คำสั่งรีนโปรแกรมปกติ
except ระบุกรีณีที่ผิดพลาด:
    คำสั่งที่ทำงานตอนโปรแกรมทำงานผิดพลาดกรณีที่เรากำหนด
'''
try:
    a=int(input(":"))
    b=int(input(":"))
    c=a/b
    print(c)
except ValueError:
    print("ป้อนเฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใช้เลข 0")
except TypeError:
    print("ชนิดข้อมูลไม่ถูกต้อง")
