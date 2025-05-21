#lambda function คือ ฟังชั่นที่เรายังไม่คืดชื่อ
'''
lambda arguments : expession
'''
a=lambda a:a
b=lambda a,b:a+b
print(a(1))
print(b(1,2))
print('')
def c(c):
    print(c)
    #c=ตัวเลข
    #x=เลขคูณ
    return lambda s:c*s #รีเทิร์น lambda กลับไปที่ x
x=c(2)
y=x(3) #กำหนดค่าให้ s ใน lambda
print(y)
