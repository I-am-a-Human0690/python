#Exeption
    #try
'''
try:
    คำสั่งรีนโปรแกรมปกติ
except:
    คำสั่งที่ทำงานตอนโปรแกรมทำงานผิดพลาด ไม่ว่าจะผิดพลาดอะไรก้ตาม
'''
try:
    a=int(input(":"))
    b=int(input(":"))
    c=a+b
    print(c)
except:
    print("ผิดพลาด")
    
try:
    a=int(input(":"))
    b=int(input(":"))
    c=a+b
    print(c)
except Exception:
    print("ผิดพลาด")