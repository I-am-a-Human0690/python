#การทำงานร่วมกับ list
a=(1,2,3)
b=[1,2,3]
#1
b=tuple(b)
a+=b
b=list(b)
print(a)
#2
c=(1,2,3)
d=[1,2,3]
c+=tuple(d)
print(c)
print(type(d))