#แบ่งข้อมูล array
import numpy as np 
a=np.arange(1,21)
print(a)
print(np.split(a,5))
#print(np.split(a,6))ไม่ลงตัว
print("")
#2 มิติ
a=a.reshape(4,5)
print(a)
print(np.hsplit(a,5))
print('')
#print(np.hsplit(a,4))ไม่ลงตัว
print(np.vsplit(a,4))
