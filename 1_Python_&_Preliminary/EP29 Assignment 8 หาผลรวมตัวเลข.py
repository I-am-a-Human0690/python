#หาผลรวมตัวเลข
a=1#จำนวนรอบ
sumation=0#เก็บผลรวบ
average=0#ผลรวม/รอบ
b=int(input("กรอกจำนวนรอบ = "))
while a<=b:
    sumation+=a
    print("จำนวนรอบ = ",a," จำนวนผลรวม = ",sumation)
    a+=1
average=sumation/b
print("ผลรวมบวกเลข = ",sumation)
print("ค่าเแลี่ย = ",average)