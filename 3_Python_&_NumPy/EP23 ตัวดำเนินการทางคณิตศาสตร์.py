#ตัวดำเนินการทางคณิตศาสตร์
import numpy as np
a=np.arange(1,5)
b=np.arange(1,5)
print(a)
print("")
print(a+1) #อื่นๆก็ได้
print("")
print(a+[1])
print("")
print(a+b)
print('')

c=np.array([[1,1,1],[1,1,1],[1,1,1]])
d=np.array([[1,1,1],[1,1,1]])
e=np.array([1,1,1])
#print(c+d) #บวกไม่ได้
print(c+e) #อื่นๆก็ได้
print(d+e)