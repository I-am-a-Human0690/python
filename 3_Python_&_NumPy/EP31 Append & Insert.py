#insert 1 มิติ
import numpy as np 
a=np.array([1,2,3,4])
print(np.insert(a,1,100))  #(,index,)
print(np.insert(a,(1,3),100))
print(np.insert(a,[1,3],100))
print(a)