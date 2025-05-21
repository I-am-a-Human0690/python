#แยกตัวเลขคู่คี่
a=[]
c=[]#เลขคู่
d=[]#เลขคี่
while True:
    b=int(input("ป้อนตัวเลข : "))
    if b<0:
        break
    if b%2==0:
        c.append(b)
    else:
        d.append(b)
    a.append(b)
print("ตัวเลขทั้งหมด",a)
print("เลขคู่",c)
print("เลขคี่",d)