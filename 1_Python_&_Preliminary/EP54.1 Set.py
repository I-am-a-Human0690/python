#set จะใส่ข้อมูลซ้ำกันไม่ได้ จะขึ้นแค่ตัวเดียว  #เรียกแต่ละครั้งจะเรียกลำดับไม่แน่นอน
#แบบปกติ
a={1,2,3,1,"2",2.1,True,} #True จะไม่ขึ้น
a3={1,2,3,1,"2",2.1,2==2,} #True จะไม่ขึ้น
a1={1,2,3,1,"2",2.1,False,} #แต่ False จะขึ้น
a2={1,2,3,1,"2",2.1,2==1,} #แต่ False จะขึ้น
b={"1","2","3"}
print(a,"\t",a3,"\t",a1,"\t",a2)
print(b,end='')
print(type(b))
#print(a[0]) #ไม่ได้เพราะ set มีลำดับไม่แน่นอน

#constructor
b=set(["1","2","3"])
x=set["1","2","3","5"]#<class 'types.GenericAlias'>
c=set({"1","2","3"})
#c1=set("1","2","3") ไม่ได้
#c=set{"1","2","3"} ไม่ได้
print(b,end="")
print(type(b))
print(x,end="")
print(type(x))
print(c,end="")
print(type(c))

#เปลี่ยน list เป็น set
d=(1,2,3)
e=set(d)
print(type(e))
#เปลี่ยน list เป็น set
d={1,2,3}
e=list(d)
print(type(e))

