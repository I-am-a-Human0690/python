               #BreK = ออกจาก loop
               #Continue = ข้ามรอบนี้
#BreK = ออกจาก loop
'''
a=1
while a<=10:
    print("รอบที่ : ",a)
    if a==5:
        break
    a+=1
else:
    print("จบโปรแกรม")
print("จบโปรแกรม")
'''
'''
#Continue = ข้ามรอบนี้
b=1
while b<=10:
     b+=1
     if b==5:
        continue
     print("รอบที่ : ",b)
'''
'''
#Continue = ข้ามรอบนี้
c=1
while c<=10:
     c+=1
     if c%2 != 0:
        continue
     print("รอบที่ : ",c)
'''
for d in range(1,10):
     if d%2 != 0:
         continue
     print("รอบที่ : ",d)


