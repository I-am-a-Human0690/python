import cv2 
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/39.png",0)

#thresh ค่าจุดแบ่ง                      #170 ค่าจุดแบ่ง 255ค่า Max
#THRESH_BINARY_INV ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 0 ที่เหลือเป็น 255 #33
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

#สร้างเลข 1 2*2
kernel = np.ones((2,2),np.uint8) 

#39
#การขยายภาพ
dilation = cv2.dilate(result,kernel,iterations=5) #iterations ทำซ้ำหรือกรอง

#การกร่อนภาพ
erosion = cv2.erode(result,kernel,iterations=7)
#ทำงานร่วมกัน 
#erosion = cv2.erode(dilation,kernel,iterations=7)

#opening ใช้กำจัดวัตุขนานเล็ก
opening = cv2.morphologyEx(result,cv2.MORPH_OPEN,kernel,iterations=3)
#ทำงานร่วมกัน 
#opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel,iterations=7)

titles = ["ORIGINAL","THRESH","DILATION","EROSION","OPENING"]
images = [img,result,dilation,erosion,opening]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()