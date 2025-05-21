'''
การกระจายข้อมูล scatter
'''
#เป็นการสุ่มข้อมูลเพื่อมายกตัวอย่าง
import numpy as np
import matplotlib.pyplot as plt
rng=np.random
x=rng.rand(50)*10
y=2*x+rng.randn(50)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#y=ax+c c=ค่าrandom