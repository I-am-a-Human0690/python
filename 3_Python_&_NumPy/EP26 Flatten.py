#flatten  แปลงเป็น 1 มิติ ไม่ถาวร
#ravel
import numpy as np
a=np.array([[1,1,1],[1,1,1],[1,1,1]])
b=a.flatten()
print(b)
print(a)
print('')
c=a.ravel()
c[0]=2 #aจะเปลี่ยน
print(a) 