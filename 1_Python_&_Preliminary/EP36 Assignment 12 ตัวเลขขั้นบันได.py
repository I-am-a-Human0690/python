max,min=0,9999999999
while(True):
    number=int(input("กรอกตัวเลข : "))
    if(number<0):
        break
    if number>max:
        max=number
    if number<min:
        min=number
print("ค่าที่มากที่สุด : ",max)
print("ค่าที่น้อยที่สุด : ",min)