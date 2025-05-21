#การส่งค่าเข้ามาที่ function
def a(a): 
    print(a)
a("a1")
a("b")
a("1")
print('')

def b(a):
    print("b"+str(a))
b(1)
print('')

def c(a,b):
    print(a,b)
c("a",1)
print('')

def d(a,b):
    print(a,b)
a=1
b="a"
d(a,b)
print('.............')
#ชื่อเซ้ำกัน
def j(a):
    print("1")
def j(b):
    print("a")
j(1)
