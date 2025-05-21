print(20-(5+10))


def say_hi(name='John Doe'):
    print("Hello %s" % name)
say_hi()   # Hello John Doe

a=[]
print(a == [])

b=[1]
del b[0]
print(b == [])


t = 'ssdsds'
print(f'{t}')
print(f'{t:#<20}')
print(f'{t:_>20}')
print(f'{t:.^20}')

c=[1,3,7,800,'d']
print(c[0])
print("{:<20}{:<10}{:<10}".format('กอดดก','กดิกดิ','sกหอกหอกห'))
print("{:<20}{:<10}{:<10}".format('กดิดกิกด',777,5555))
print("{:<20}{:<10}{:<10}".format('sss534dsbwbwbe',c[0],c[3]))
print("{:^20}{:^10}{:^10}aaaa".format('sss','ssdsc','sdvdsv'))
print("{:20}{:<10}{:10}aaaa2".format('sss534dsbwbwbe','scscss','sdvds'))
#{:(ชิดซ้ายขวา)(จำนวนพื้นที่)}   ถ้าใช้ภาษาไทยจะไม่ตรง
#^ตรงกลาง
e=[1,4,5,7,7]
for i in range(len(e)):
    print(i)

#อีกวิธีหนึ่งคือการใช้รายการคอมเพรสชัน (list comprehension) เพื่อสร้างรายการใหม่ที่ไม่รวม 'a' แต่ไม่ได้ลบ 'a' ออกจาก number2 ตัวเอง:
number2 = ['a', 'b', 'c']
number2 = [item for item in number2 if item != 'a']
print(number2)
v=[]
v.append(0)
print(v)
