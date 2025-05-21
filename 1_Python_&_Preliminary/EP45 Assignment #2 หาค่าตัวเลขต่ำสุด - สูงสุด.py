#หาค่ามากสุดน้อย น้อยสุด
a=[]
while True:
    b=int(input("ป้อนตัวเลข : "))
    if b<0:
        break
    a.append(b)
print("ทั้งหมด",a)
print("ค่ามากสุด",max(a))
print("ค่าน้อยสุด",min(a))
print("ผลรวม",sum(a))