#ชนิดข้อมูล (Data Type)
'''
ชนิดข้อมูลหลักๆ ที่ใช้ใน Numpy
1. Integer
2. Float
3. String
4. Boolean
5. Complex
6. Object
'''
import numpy as np
a=np.array([1,2,3])
print(a.dtype)
b=np.array([1,2,3],dtype="int")
print(b.dtype)
c=np.array([1,2,3],dtype="float")
print(c.dtype)
d=np.array([1,2,3],dtype="complex")
print(d.dtype)
e=np.array([[1,2,3],[4,5,6]],dtype="float")
print(e.dtype)