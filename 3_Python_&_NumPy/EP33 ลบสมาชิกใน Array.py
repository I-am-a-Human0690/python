#ลบสมาชิก
import numpy as np 
a=np.arange(1,15)
print(a)
print(np.delete(a,0))
print(a)
print('')

b=np.arange(1,13).reshape(4,3)
print(b)
print('')
print(np.delete(b,0,axis=0))
print(np.delete(b,0,axis=1))
print('')
print(b)