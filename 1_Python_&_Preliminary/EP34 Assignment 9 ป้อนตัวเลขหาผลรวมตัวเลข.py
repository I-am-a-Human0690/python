start,stop,sum,avg=1,5,0,0
while(start<=stop):
    number=int(input("กรอกตัวเลข : "))
    sum+=number
    start+=1
avg=sum/stop
print("ผลรวมเท่ากับ = ",sum)
print("เฉลี่ย = ",avg)
