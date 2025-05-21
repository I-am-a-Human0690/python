#เกมทายเลข #คำสั่ง random
import random
myrandom=random.randrange(1,7)
k=1
print(myrandom)
print("คุณมีโอกาศตอบ 3 ครั้ง \n")
while True:
     number=int(input("กรอกตัวเลข : "))
     correct=(number==myrandom)
     if not correct:
         if(number>myrandom):
             print("น้อยกว่า")
         if(number<myrandom):
             print("มากกว่า")
     if correct:
         print("ตอบถูกรับไปเลย 1 ล้านบาท")
         break
     if number<0 or k==3:
         break
     k+=1
if not correct:
    print("เสียใจด้วยนะ")
    print("เฉลย = ",myrandom)
'''
b=1
while b<4:
    a=int(input("กรอกตัวเลข : "))
    if a==myrandom:
        print("ถูก")
    else:
        print("ผิด")
    b+=1
'''