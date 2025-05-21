#slice Array 3 มิติ
                  #มิติ                #แถว                    คลอลัม
#           a[start:stop:step ,  start:stop:step   ,   start:stop:step]
import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a)
print('00000')
print(a[0,0:1,0:1])
print(a[1,0:1,0:1])
print(a[0:1,0:1,0:1])