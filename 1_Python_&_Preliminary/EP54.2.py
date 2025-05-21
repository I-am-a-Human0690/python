#เพิ่มข้อมูลสมาชิก
a={1,2,3,True,1,"2",2.1,False}
a.add(7)
print(a,type(a))
#เพิ่มข้อมูลสมาชิกหลายตัว
b=["5","9"]
a.update(b)
print(a)
# loop
for c in a:
    print(c,end="")
print(" ")

#แสดงจำนวนสมาชิก
print(len(a))

#if
if 1 in a:
    print("มี")
else:
    print("ไม่มี")
#หรือ
print(1 in a)

#remove discard
x={1,2,3,4}
print(x)
x.remove(1) #ถ้าไม่มีตัวนั้นจะ error
x.discard(5) #ลบเหมือนกันแต่ถ้าไม่มีจะ ไม่error #ใช้กับ listไม่ได้
print(x)