
# *ชื่อตัวแปร เป็นชนิดข้อมูลเป็น tuple เก็บค่าได้ไม่จำกัด
def a1(a):
    print(a,type(a))
def a2(a,b):
    print(a,b,type(a))
def a3(a,b,c):
    print(a,b,c)
a1(1)
a2("a",2)
a3(1,2,3)
print('')

def b1(*b1):
    print(type(b1),b1[0],type(b1[0]))#ข้อมูลเป็น int
b1(1,2,3)
aca=[1,2,3]
b1(aca)
print('')

def b2(*b1):
    print(b1[0]+b1[1])
xy=1
b2(xy,2,3) #b2(xy,a="a",3)  ไม่ได้
print('')

def b3(*b1):            
    b=0                                    
    for a in b1:                               
        b+=a
    print(b)
b3(1,2,3)
print('')

def b4(*b1):
    b=0
    for a in range(len(b1)):
        b+=b1[a]
    print(b)
b4(1,2,3)

print('b5')
def b5(*b1):
    print(b1,type(b1))
    print(b1[0],type(b1[0]))
xv=[1,2,4]
b5(xv)
