#forzenset คือ ทำให้ set แก้ไขและเพิ่มข้อมูลไม่ได้
a=set([1,2,3])
a.add(4)
a.discard(2)

b=frozenset([1,2,3])
print(type(b))
#b.add(4)   ไม่ได้
#b.discard(2)   ไม่ได้
b=set(b)
print(type(b))
b.add(4)
b.discard(2)
print(b)