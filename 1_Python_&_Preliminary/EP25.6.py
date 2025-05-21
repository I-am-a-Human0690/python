#เจาะลึกพังชั่น string(str)
#เช็คข้อความว่ามีหรือป่าว
name=("sitthikon")
x="sitt"in name
print(x)
if x:#ถ้า x ไม่เป็นจะไม่ทำงาน
    name=name.replace("sitt","Sito")
print(name)

name2=("sitthikon")
a="sitt" not in name2#ทำให้ผลเป็นตรงข้าม
print(a)
if a:#aไม่เป็นจะจึงไม่ทำงาน
    name2=name2.replace("sitt","Sito")
print(name2)