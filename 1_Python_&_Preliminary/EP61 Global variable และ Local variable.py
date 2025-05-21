 #Global variable โปรแกรมหลัก / Local variable โปรแกรมย่อย

#Local 
def a():
    b=1#bใช้ได้เฉพาะโปรแกรมย่อย
    print("b")
#Global 
b=2
a()
print(b)

print('')

#Local
def x():
    y=1
    print("a")
#Global 
y=2
x()
print(y)

print('Global Keyword')
x=1
print(x)
def c():
    x=0#Local
    print(x)

c()
print(x)