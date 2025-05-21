#ตัวกรอง Convolution ด้วย #median #นิยมใช้ 3*3 5*5
#44 คำอธิบายแต่ละอันแบบละเอียด
import cv2
import numpy as np
import matplotlib.pyplot as plt

#original
img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/45.1.png")

#Filter2D  ##ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ
filter2d = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

#Mean Filte #ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ
mean = cv2.blur(img,(5,5))

#Median Filter #ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ 
mblur=cv2.medianBlur(img,5)

#Gaussian Filter #ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ 
gblur = cv2.GaussianBlur(img,(5,5),1)

titles = ["ORIGINAL","FILTER2D","MEAN","MEDIAN BLUR","GAUSSIAN BLUR"]
images = [img,filter2d,mean,mblur,gblur]

for  i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()