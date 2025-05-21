#tuple
#เก็บได้หลายตัวและแก้ไขไม่ได้ ()
#การนิยาม, #constructor
a=(1,2.1,True,"a",2<1)
b=[1,2.1,True,"a",2<1]
c=tuple((1,2.1,True,"a"))
d=list([1,2.1,True,"a",2<1])
e=list[1,2.1,True,"a",2<1]
f=1,2.1,True,"a",2<1

b[0]="a"#แก้ไขได้
#แก้ไขไม่ได้a[0]="a"
print(type(a),end="")
print(a)
print(type(b),end="")
print(b)
print(type(c),end="")
print(c)
print(type(d),end="")
print(d)
print(type(e),end="")
print(e)
print(type(f),end="")
print(f)