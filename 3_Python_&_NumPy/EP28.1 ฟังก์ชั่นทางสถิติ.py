#ต่าทางสถิติ
import numpy as np
a=np.array([1,2,3,4,5,6])
print(a.sum())
print(a.prod())#ห่าค่าคูณ
print(a.mean())#ค่าเฉลี่ย
print(a.max())
print(a.min())
print(a.argmax())#หาตำแหน่ง index ค่าที่มากที่สุด

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.min(b,axis=0))
print(np.min(b,axis=1))
print(np.max(b,axis=1))