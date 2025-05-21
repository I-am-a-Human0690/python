a=dict({"red":"สีแดง","blue":"สีฟ้า"})
b=dict({"red":"สีแดง","blue":"สีฟ้า"})
b=a.copy()
print(b)
print('')

#a.pop()#ไม่ได้
a.pop("blue")
print(a)
print('')
a.update({"yellow":"สีเหลือง","red":"สีเขียว"})
print(a)
print('')
a.popitem() #ลบตัวที่เพิ่มล่าสุดหรือตัวท้ายสุด  ไม่นำตัวที่แก้ไข
print(a)
print('')
b.clear #ไม่ได้
print(b)
print('')
del a
print(a)