#recursive function ใช้แก้ปัญหาที่ซ้ำซ้อน
'''
def a():
    print("a")
    a()             
a()        #ทำซ้ำไปเรื่อยๆ
'''
'''
หาจุดวนซ้ำ
หาจุดออกจาก function (return)
ต้องมี parameter
1-10 ไม่ต้องใช้ loop
'''
def b(a):
    print(a)
    if a==10:
        return
    a+=1
    b(a)
b(1)
print('')
def c(a):
    if a == 1:
        return a
    else:
        return a+c(a-1)
x=c(5)
print(x)
'''
5
5+c(5-1)
5+4+c(4-1)
5+4+3+c(3-1)
5+4+3+2+c(2-1)
5+4+3+2+1



'''