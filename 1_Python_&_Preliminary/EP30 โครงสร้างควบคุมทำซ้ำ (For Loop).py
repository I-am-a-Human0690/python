#โครงสร้างควบคุมแบบทำซ้ำ for
#for i in range()#(start,stop,step)
a=0
c=0
x=0
s=0
b=1
for b in range(3):#ถ้าไม่ระบุ start จะเริ่มจาก 0
    a+=b
    print("รอบที่ = ",b,"a = ",a)
print("ผลรวม = ",a)
for e in range(1,10,2):
    c+=e
    print("รอบที่ = ",e,"c = ",c)
print("ผลรวม = ",c)
for g in range(10,0,-2):
    x+=g
    print("รอบที่ = ",g,"x = ",x)
print("ผลรวม = ",x)
for d in range(-5,5,2):
    s+=d
    print("รอบที่ = ",d,"s = ",s)
print("ผลรวม = ",s)

