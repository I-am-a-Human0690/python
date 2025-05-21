#สร้าง array 0,1 มิติ
'''
import numpy as np
arr=np.array(1)
arr
array(1)
arr=np.array(2)
arr
array(2)
arr.ndim
0
a=np.array([1,2,3])
a
array([1, 2, 3])
a.ndim
1
li=[1,2,3,4]
b=np.array(li)
b
array([1, 2, 3, 4])
b.ndim
1
tu=(1,2,3,4,5,6)
c=np.array(tu)
c
array([1, 2, 3, 4, 5, 6])

'''
import numpy as np
arr=np.array(1)
print(arr)

arr=np.array(2)
print(arr)
print(arr.ndim)

a=np.array([1,2,3])
print(a,type(a))

x=np.array((1,2,3))
print(x,type(x))

print(a.ndim)
li=[1,2,3,4]

b=np.array(li)
print(b,type(b))
print(b.ndim)

tu=(1,2,3,4,5,6)
c=np.array(tu)
print(c,type(c))


