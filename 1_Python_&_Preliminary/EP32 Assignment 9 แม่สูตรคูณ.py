#สูตรคูณ
'''
a=2
while a<=12:
    print("แม่ :  ",a)
    b=2
    while b<=12:
        print(a,"*",b," = ",a*b)
        b+=1
    a+=1
'''
'''
start=int(input("กรอกแม่สูตรคูณเริ่มต้น : "))
stop=int(input("กรอกแม่สูตรคูณแม่สุดท้าย : "))
while start<=stop:
    print("แม่ :  ",start)
    b=2
    while b<=12:
        print(start,"*",b," = ",start*b)
        b+=1
    start+=1
'''
'''
for c in range(2,13):
    print("แม่ : ",c)
    for d in range(2,13):
        print(c,"*",d," = ",c*d)
'''
start=int(input("กรอกแม่สูตรคูณเริ่มต้น : "))
stop=int(input("กรอกแม่สูตรคูณแม่สุดท้าย : "))
for c in range(start,stop+1):
    print("แม่ : ",c)
    for d in range(2,13):
        print(c,"*",d," = ",c*d)
