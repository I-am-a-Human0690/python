#Sobel Method
import cv2 
import matplotlib.pyplot as plt


img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/50.jpg",0)
#Sobel(img,-1,ขอบแกน x แนวนอน,ขอบแกน y แนวตั้ง)
sobelX = cv2.Sobel(img,-1,1,0)
sobelY = cv2.Sobel(img,-1,0,1) 
sobelXY = cv2.bitwise_or(sobelX,sobelY)

images = [img,sobelX,sobelY,sobelXY]
titles = ["Original","SobelX","SobelY","SobelXY"]

for  i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()