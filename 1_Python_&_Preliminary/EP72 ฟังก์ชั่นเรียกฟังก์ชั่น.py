#ฟังชั่นเรียกฟังชั่น
def a():
    print("a")
def b():
    a()
    print("b")
b()
print('')

def c(a,b,c):
    x=d(a,b)
    y=d(x,c)
    return y

def d(a,b):
    if a>b:
        return a
    else:
        return b

print(c(10,20,30))