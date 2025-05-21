sum=0
'''
while(sum<100):
    number=int(input("กรอกตัวเลข : "))
    sum+=number
    print("ผลรวมเท่ากับ = ",sum)
print("จบโปรแกรม")
'''
while(True):
    number=int(input("กรอกตัวเลข : "))
    sum+=number
    if(sum>100):
        break
    print("ผลรวมเท่ากับ = ",sum)
print("จบโปรแกรม")