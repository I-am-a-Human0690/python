a=[0,1,2,3]
a2=[1,0,0,0]
n=0

def f1(c,b,e):
    c[0]+=e[0]
    c[1]+=1
    c[2]=5
    e=[1,2,3,4]
    b+=1

f1(a,n,a2)
print(a)
print(a2)
print(n)

#print(3//2)