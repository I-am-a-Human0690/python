#identity ข้อจำกัด แถวและคลอลัมต้องเท่ากัน
import numpy as np
print(np.identity(4))
print(np.identity(4,dtype="int"))
print('1')
print(np.eye(4))
print(np.eye(3,4))
#ย้ายเลข 1
print('2')
print(np.eye(4,k=1))
print(np.eye(4,k=-1))

print('000')
print(np.eye(2,3,4))#3มิติไม่ได้
print(np.identity(4))
