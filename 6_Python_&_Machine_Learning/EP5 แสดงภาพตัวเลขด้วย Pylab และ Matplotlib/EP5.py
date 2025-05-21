import pylab
from sklearn import datasets
digit_dataset=datasets.load_digits()
print(digit_dataset.target[0])#ระบุเลข
pylab.imshow(digit_dataset.images[0],cmap=pylab.cm.gray_r)
pylab.show()
#ถ้าอยากแสดงหลายๆรูปให้ใช้ loop
#ใช้ matplotlib แสดงภาพก็ได้
