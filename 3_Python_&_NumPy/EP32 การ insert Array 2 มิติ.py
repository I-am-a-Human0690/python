#insert 2 มิติ
import numpy as np 
a=np.array([[1,2],[3,4]])
print(np.insert(a,1,100,axis=0))
print(np.insert(a,1,(10,),axis=0))
print(np.insert(a,1,[10,20],axis=0))
print(np.insert(a,(1,2),[10,20],axis=0))
print(a)
print('')

print(np.insert(a,1,100,axis=1))
print(np.insert(a,1,(10,),axis=1))
print(np.insert(a,1,[10,20],axis=1))
print(np.insert(a,(1,2),[10,20],axis=1))
print(a)