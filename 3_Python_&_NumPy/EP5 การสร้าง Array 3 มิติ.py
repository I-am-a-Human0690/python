#สร้าง array 3 มิติ
'''
import numpy as np
b=np.array([[1,2,3],[4,5,6]])
b
array([[1, 2, 3],
       [4, 5, 6]])
c=np.array([[[1,2,3],[4,5,6]]])
c
array([[[1, 2, 3],
        [4, 5, 6]]])
b.ndim
2
c.ndim
3
'''
import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print(b)

c=np.array([[[1,2,3],[4,5,6]]])
print(c)

print(b.ndim)

print(c.ndim)

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x)
