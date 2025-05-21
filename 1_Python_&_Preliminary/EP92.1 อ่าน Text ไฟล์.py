#open("ชื่อไฟล์","โหมด","รหัส") ไม่ระบุก้ได้
#Mode	Description
# r	    เปิดไฟล์เพื่ออ่านข้อมูลจากไฟล์
# w	    เปิดไฟล์เพื่อเขียนข้อมูลลงบนไฟล์
# a	    เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายไฟล์เดิม
# r+	เปิดไฟล์เพื่ออ่านและเขียนข้อมูล
# w+	เปิดไฟล์เพื่ออ่านและเขียนข้อมูล ถ้าหากมีไฟล์เดิมอยู่โปรแกรมจะเขียนทับ
# a+	เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
# b	    เปิดไฟล์ใน Binary mode เช่น rb wb ab rb+ wb+ หรือ ab+

#"รหัส" คือ ระบุก้ได้ไม่ระบุก้ได้ ภาษาอื่นๆที่ต้องเอนโค้ดเพื่ออ่าน 

# a=open("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\1Python_&_Preliminary\\EP92.2.txt","r")
a=open('Python/1_Python_&_Preliminary/EP92.2.txt','r')
#a=open('Python/1_Python_&_Preliminary/EP92.2.txt','r') #แบบนี้ก้ได้
b=open('Python/1_Python_&_Preliminary/EP92.3.txt','r',encoding="utf-8")#"utf-8"สำหรับภาษาไทย
c=open('Python/1_Python_&_Preliminary/EP92.3.txt','r')

print(a)
print(a.read())
print(a.read())#ซ้ำกันจะไม่แสดง
print('..')

print(b)
print(b.read())
print('...')

print(c.read(5))#5ตัวตัวแรก
print(c.read(20))
print('')

try:
    y=open('./Python/1Python_&_Preliminary/EP92.2.txt',"r")
    print(y.read())
except Exception as x:
    print(x)


