#การแก้ไขชื่อข้อมูล
#ชื่อตัวแปร [index] = ข้อมูลที่แก้ไข
number2=[1,2,3,4,5]

print("ก่อนแก้ไข : ",number2)
number2[2]=1
number2[-1]="s"
print("หลังแก้ไข : ",number2)

#หา index
number3=[1,2,3,4,5]
a=number3.index(3)#หาตำแหน่งจะเจอแค่ตัวแรก #1อยู่ index ที่ 3
print(a)

number2=["s","v"]
number2["s"]="r"
print(number2)