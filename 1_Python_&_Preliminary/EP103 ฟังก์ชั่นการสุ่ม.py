#random
import random
a=random.random() #0.0-ก่อน 1.0
print(a)
#a2=random.random(1,10) ไม่ได้
#print(a2)
print('')

b=random.uniform(-5,10) #-5 - ก่อน 10
print("%.0f"%(b))
print('')

for i in range(10):
    c=random.randrange(1,10,2) #สุ่มว่าจะเพิ่มกี่สเต็ปและใช้ตัว start โดยไม่เพิ่มสเต็ปเกิน 10 #เอาไว้สุ่มเลขคู่คี่
    print(c)
print('')

d=random.randint(-4,5) #-4 - 5
print(d)
print('')

e=[1,2,3,"a","b"]
for i in range(3):
     random.shuffle(e) #f=random.shuffle(e) ไม่ได้ เพราะเป็นการสุ่มเรียงลำดับใน e แล้วปริ้น e
     print(e)
print(e) #การเรียงลำดับจะตรงกับ for อันสุดท้าย
print('')

g=[1,2,3,"a","b"]
for i in range(3):
     h=random.choice(g) 
     #h=random.choice([1,2,3,"a","b"]) #แบบนี้ก็ได้
     #h=random.choice(1,2,3,"a","b") #แบบนี้ไม่ได้เพราะ ข้อมูลไม่ใช้ str
     j=random.choice("123ab")        #แบบนี้ก็ได้
     print(h,"\n",j)
