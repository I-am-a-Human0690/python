#assignment
def a(a):
    b,c=0,0
    for i in a:
        b+=i
    c=b%len(a)
    return b,c
x=[1,2,3,4]
z,y=a(x)
print(z)
print(y)