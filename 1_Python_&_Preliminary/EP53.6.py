#การนับจำนวนสมาชิก
a=(1,2.1,"a",2<1)
print(len(a)) #0-7 = 8 ตัว
#การทำงานร่วมกับ loop 
for b in range(len(a)):
    print(a[b])
'''
for c in range(a):#ไม่ได้
    print(a[c])
'''
for c in a:#แบบนี้ก้ได้
    print(c)


