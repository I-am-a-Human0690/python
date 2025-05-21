#remove,pop,del,clear
#remove(ตัวที่ต้องการลบ)
a=[1,2,3,4,5,6,]
b=[1,2,3,4,5,6]
a.remove(2)
print(a)
#pop(index) ไม่ใส่เทากับลบตัวสุดท้าย
a.pop()#ลบตัวสุดท้าย
print(a)
#del
del a[0]
del b #ลบตัวแปรออกไปเลย
print(a)
#clear ลบข้างในทั้งหมดแต่ตัวแปรยังอยู่
a.clear()
print(a)