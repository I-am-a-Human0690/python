#ไม่มีการรับค่าและส่งค่าคืน return
'''
def a():
'''
# 2 มีการรับค่า
'''
def a(a,b):
'''
# 3  มีการรับค่าและส่งค่าและส่งออก
def a(a,b):
    return a+b
# a(10,20) จะไม่ return เพราะ ไม่ print()
x=a(10,20)
print(x)
#หรือ
print(a(10,20))
print('')

# 4 ไม่มีการรับค่า แต่มีการส่งค่าออก
def b():
    return 500
z=b()
print(z)
#หรือ
print(b())
print('')

#ทดลอง
def c():
    print(2)  #none คือไม่มีค่า return
v=c()
print(v)
#หรือ
print(c())
print('')

def e(a):
    if a == 9999:return "ถูกหวย"
    else:return "ไม่ถูกหวย"
print(e(9999))