#numpy Attribute shape zine itemsize
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="complex")
c=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(c.ndim)

print(a.shape,a.size)
print(b.shape,b.size)
print(x.shape,x.size)
print(c.shape,c.size)

print(a.dtype)  #32 บิท
print(a.itemsize)  #1 ไบร์ = 8 บิท  32/8 = 4

print(b.dtype)
print(b.itemsize)

print(x.dtype) #128
print(x.itemsize) #128/8

print(c.dtype)
print(c.itemsize)