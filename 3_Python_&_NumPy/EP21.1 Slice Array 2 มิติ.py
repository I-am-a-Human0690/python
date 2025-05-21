#slice Array 2 มิติ
       #แถว                    คลอลัม
#a[start:stop:step   ,   start:stop:step]

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:,:])
print('')

print(a[::-1,:])
print('')

print(a[::-1,::-1])
print('')

print(a[1:,1:])  #5 6  8 9
print('')

print(a[:2,:])  #123 456
print('')

print(a[1:2,1:2]) #5
print('')

print(a[::2,:]) #123 789
print('')

print(a[:,::2]) #13 46 79
print('')

print(a[::2,::2]) #13 79
print('')

print(a[::-2,::-2]) #97 31
print('')

print(a[::-2,::2]) #79 13
print('')