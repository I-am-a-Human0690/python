#การเข้าถึงสมาชิก Array 3 มิติ (Index)
import numpy as np
a=np.array([[[1,2,3],[4,5,6]]])
print(a)
print(a.ndim)
print('')
print(a[0][0][1])
print('')
#a[dept][row][column]
#a[ชั้น][แถว][คลอลัม]
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(b)
print(b[1][0][1])