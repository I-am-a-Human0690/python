#https://medium.com/super-ai-engineer/%E0%B8%A1%E0%B8%B2%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%9A-morphological-image-processing-%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%94%E0%B8%B5%E0%B8%81%E0%B8%A7%E0%B9%88%E0%B8%B2-da5ea9b7bbad
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/39.png",0)

#thresh ค่าจุดแบ่ง                      #170 ค่าจุดแบ่ง 255ค่า Max
#THRESH_BINARY_INV ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 0 ที่เหลือเป็น 255 #33
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

titles = ["ORIGINAL","THRESH"]
images = [img,result]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()