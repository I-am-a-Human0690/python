#การใช้ del การลบแบบlist
a=(1,2,3)
b=(1,2,3)
#del b[0]#ไม่ได้
del b #ลบทั้งตัวแปรเลย
a=list(a)
a.remove(3)
del a[0]
a=tuple(a)
print(a)