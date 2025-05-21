a=[2,2,3,1,1]
b=a.count(1)#หาจำนวน
c=a.index(1)#หาตำแหน่งจะเจอแค่ตัวแรก #1อยู่ index ที่ 3
print(c)


e=["asdasd",7,2,"a"]
print(len(e))
print('')
# a1=["dgjjm",1,2,3]
a1="sfsgdg"
for i in  range(len(a1)):
    print(i)

a2=None
print(a2)

a3=2.11112
print("dfgfd {:.2f}".format(a3))
print(f"{"fvdfvdf":15}{a3:>15}".format(a3))
#BMI=float("%.1f"%(BMI)) #แปลงเป็น 1 ตำแหน่ง
#BMI=float("{:.1f}".format(BMI)) #แปลงเป็น 1 ตำแหน่งprint(BMI)


a4=[[1,2],[4,5]]
print(a4,type(a4),a4[1])
a5=([1,2],[4,5])
print(a5,type(a5),a5[1])

member = str.upper(input("T/F: "))
#if member == "T" or member == "t": #if member in "T","ts"

num1 , num2 = eval ( input ( ' Please enter number 1 , number 2 : ' ) )
print ( num1 , ' + ' , num2 , ' = ' , num1 + num2 )
a=[]
for i in range(3):
     a.append(exec ( input ( " >>> " ) )) #ใส่ตัวเลขเลยเลื่อยๆ
print(a)

#exec("print(111)\nprint(111)")