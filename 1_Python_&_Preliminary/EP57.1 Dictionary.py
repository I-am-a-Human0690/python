#Dictionary
# list , tuple
a1=[1,2,3]
a2=(1,2,3)
print(a1[0])
print(a2[2])
print(" ")
#list , tuple > index , value
#Dictionary > key , value
a3=dict(a=1,a1=2,cat="cat",true="จริง",false="ไม่จริง") #constructor key ใส่ "" กับ ตัวเลขไม่ได้ True False ไม่ได้ #str int ไม่ได้
#a3=dict("a"=1,"a1"=2,"cat"="cat",1=1)ไม่ได้ 
print(a3,type(a3))
print(a3["a"])
print(a3["cat"])
print(a3.get("a"))
#print(a3[1])#ไม่ได้
print('')

a4={"red":"สีแดง",1:"a",1.3:8,70:"a",True:"จริง",False:"ไม่จริง",False:"ไม่จริง2"}#a4={red:"สีแดง"}ไม่ได้
a5=dict({"red":"สีแดง",1:"a",1.3:8,70:"a",True:"จริง",False:"ไม่จริง"})
#a4={red:"สีแดง"}ไม่ได้
print(a4,type(a4))
print(a5,type(a5))
print(a4["red"])
print(a4[1.3])
print(a4.get("red"))
print(a4[0])# 0 1 เรียก True False
print(a4[False])
print(a5["red"])
print(a5[1.3])
print(a5.get("red"))
print(" ")