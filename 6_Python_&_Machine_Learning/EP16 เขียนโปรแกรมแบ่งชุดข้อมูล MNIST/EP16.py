from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
mnist_raw=loadmat("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\mnist-original.mat")
mnist={
"data":mnist_raw["data"].T,
"target":mnist_raw["label"][0]#"label"="target"
}
print(mnist["data"].shape)

x,y=mnist["data"],mnist["target"]

# training , test
#1-60000
#60001-70000
x_train, x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#0-9
#ส่งตำแหน่งที่ 5000 เข้าไป 5000 คือ เลข 5
#ให้เครื่องตอบกลับออกมาว่าจริงไหม