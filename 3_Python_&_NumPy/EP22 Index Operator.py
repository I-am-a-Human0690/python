#index operator
import numpy as np
a=np.arange(1,10)
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print('')

b=np.array([1,5,7])
print(a[b]) #ใช้ b ระบุตำแหน่ง index
print('1')

print(a[[0,2]]) 
        #index 0,2
print('2')

print(x[[0,2],[1]])
#   แถวที่ 0,2 คลอลัมที่ 2
print('3')

print(x[[0,2],[1,2]])
#   แถวที่ 0,2 คลอลัมที่ 1,2 = แถวที่ 0 คอลลัมที่ 1, แถวที่ 2 คอลลัมที่ 2
print('4')

print(a[a>5])
print(a[a>5]*2)
print('')

y=np.array([[-1,-2,-3],[-4,-5,-6]])
print(y[y<0]*-1)