#ตัวกรอง Convolution ด้วย Filter2D  #ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ
#นิยมใช้ 3*3 5*5
#44
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/45.1.png")

                              #kernel       #ชนิดข้อมูล / 3*3 = 9
convo1 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convo2 =cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

titles = ["ORIGINAL", "CONVOLUTION 3X3" , "CONVOLUTION 5X5"]
images = [img,convo1, convo2]

for  i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()