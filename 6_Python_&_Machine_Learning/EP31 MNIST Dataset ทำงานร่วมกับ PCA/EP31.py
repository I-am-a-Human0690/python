from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from scipy.io import loadmat
import matplotlib.pyplot as plt
mnist_raw=loadmat("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\mnist-original.mat")
mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}
x_train, x_test, y_train,y_test = train_test_split(mnist["data"],mnist["target"],random_state=0)

# print("Before = ",x_train.shape)
pca=PCA(.95)#ลดขนาดรูปภาพ #pca=PCA(.80)
#x_train=pca.fit_transform(x_train)
data=pca.fit_transform(x_train)
# print("After = " ,x_train.shape)
result=pca.inverse_transform(data)#แปลงกลับให้เป็นข้อมูลดังเดิม

#show image
plt.figure(figsize=(8,4))
#image feature 784
plt.subplot(1,2,1)
plt.imshow(mnist["data"][0].reshape(28,28),cmap=plt.cm.gray,interpolation="nearest")
plt.xlabel("784 Features")
plt.title("Original")
#image feature 95% -> 154
plt.subplot(1,2,2)
plt.imshow(result[0].reshape(28,28),cmap=plt.cm.gray,interpolation="nearest")
plt.xlabel("154 Features")
plt.title("PCA Image")
plt.show()