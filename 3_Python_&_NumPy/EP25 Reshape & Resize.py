#reshape  เปลี่ยนแค่ชั่วขณะ
#Resize  เปลี่ยนถาวร

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([1,2,3,4,5,6,7,8,9,10,11])
print(a.reshape((2,5)))
print('')
#print(b.reshape((2,6))) ไม่ได้
print(a.reshape([2,5])) 
print(a)
print('')

a.resize((2,5))
print(a)