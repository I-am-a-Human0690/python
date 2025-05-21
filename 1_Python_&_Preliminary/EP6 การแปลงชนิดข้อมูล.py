
a=10
b=20
c="30"
v="10"
p="20"
q=1.1
w=1.8
x=a+int(c)#แปลง str เป็น ing เพื่อให้คำนวณได้ และสามารถแปลงอย่างอื่นเป็นอย่างอื่นได้ด้วย
print(x)
print(type(x))
print(str(a))#แปลง ing เป็น str
z=int(c) #แปลงและเก็บไว้ในz
print(z)
c=int(c) #แปลงและเก็บทับตัวเดิม หลังจากนั้น c เท่ากับ int ไปตลอด
print(c)
print(type(c))
f=a+int(q)#ทศนิยมจะหายไป
print(f)
t=a+int(w)#ทศนิยมจะหายไปและจะไม่ปัดขึ้น
print(t)
i=str(10)+str(b)#จะเอามาต่อกันเพราะเป็น str
j="10"+str(b) #แบบนี้ก็ได้
print(j)
print(i)
print(type(i))
print(a+int(v))
print(v+p)
print(int(v+p))
print(int(v)+int(p))
print(float(a))


