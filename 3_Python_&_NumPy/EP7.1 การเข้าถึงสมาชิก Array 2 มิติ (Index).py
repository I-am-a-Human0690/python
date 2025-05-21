#การเข้าถึงสมาชิก Array 2 มิติ (Index)
'''
import numpy as np
a=np.array([1,2,3])
a
array([1, 2, 3])
a[0]
1
a[-3]
1
b=np.array([[1,2,3],[4,5,6]])
b
array([[1, 2, 3],
       [4, 5, 6]])
b[0][2]
3
b[1][2]
6
b[1][2]=8
b
array([[1, 2, 3],
       [4, 5, 8]])
a[0]=2
a
array([2, 2, 3])
b[-1][-1]
8
b[-1][-1]=10
b
array([[ 1,  2,  3],
       [ 4,  5, 10]])
'''
import numpy as np
a=np.array([1,2,3])
print(a)

print(a[0])

print(a[-3])

b=np.array([[1,2,3],[4,5,6]])
print(b)

print(b[0][2])

print(b[1][2])

b[1][2]=8
print(b)

a[0]=2
print(a)

print(b[-1][-1])

b[-1][-1]=10
print(b)
