a=dict({"red":"สีแดง","blue":"สีฟ้า"})
print(a)
#key ไม่ซ้ำ เพิ่มเข้าไป   #key ซ้ำ  แก้ไข value
a["red"]="ส"
a["red2"]="ส"
print(a)
print(" ")

a.update({"green":"สีเขียว","yellow":"สีเหลือง"})
print(a)
print(" ")

#key ไม่ซ้ำ เพิ่มเข้าไป   #key ซ้ำ  แก้ไข value
a.update({"red":"สีlucyt"}) #red ซ้ำ
print(a)