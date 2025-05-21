#นำค่า tuple ใส่ตัวแปร
print("นำค่า tuple ใส่ตัวแปร")
a=(1,2,7)
#a=b,c,d ไม่ได้
b,c,d=a
print(b,end='')
print(type(b))
print(c,end='')
print(type(c))
print(d,end='')
print(type(d))
print('')

#สลับค่า 
print("สลับค่า ")
e=(1,2)
d=(3,4)
print(e)
print(d)
e,d=d,e
print(e)
print(d)
print('')

#แปล tuple ให้เป็น str
print("แปล tuple ให้เป็น str")
f=("a","c","d")
g="".join(f)
k2="/".join(f)
print(g)
print(k2)
print('')

#reverse
print("reverse")
h=(5,6,7,9,1,3)
j=("asdawd")
#h.reverse() tuple แก้ไขไม่ได้
i=reversed(h)
print(i)
print(type(i))
print(tuple(i))#ต้องแปลงแบบนี้ก่อน แปลงเป็น list ก้ได้
print("แบบนี้ก้ได้")
print(j)
print(tuple(j))
k=tuple(reversed(j))
print(k)