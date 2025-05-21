#concatenate
import numpy as np 
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
print(np.concatenate((a,b)))
print(np.concatenate([a,b]))
print(a)
a=np.concatenate((a,b))
print(a)
print('')

print(np.append(b,10))
print(b)
b=np.append(b,10)
print(b)
print('')

c=np.array([[1,2],[3,4]])
print(np.append(c,[[10],[10]],axis=1))
print('')
print(np.append(c,[[10,10]],axis=0))
print('')
print(c)
