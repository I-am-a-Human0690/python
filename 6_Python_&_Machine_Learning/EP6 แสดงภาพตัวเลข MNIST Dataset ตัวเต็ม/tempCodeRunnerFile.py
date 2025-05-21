'''
sklearn มีข้อมูล MNIST Dataset 5620 ชุด และมีขนาด 8*8 
ต้องไปโหลดตัวเต็ม
'''
import matplotlib.pyplot as plt
from scipy.io import loadmat
mnist_raw=loadmat("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\mnist-original.mat")
print(mnist_raw)
mnist={
    "data" :mnist_raw["data"].T,# T = ทรานสโพส กลับด้านจาก 784,70000 => 70000,784
    "target":mnist_raw["label"][0]
    }
print(mnist["data"].shape)#ขนาด
x,y=mnist['data'],mnist['target']
number=x[10000]
number_image=number.reshape(28,28)
print(y[10000])
plt.imshow(
    number_image,
    cmap=plt.cm.binary,
    interpolation="nearest")
plt.show()