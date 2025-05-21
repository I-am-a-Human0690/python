# แสดงผลภาพด้วย Matplotlib
# CV2 เป็น BGR
# Matplotlib เป็น RGB #ปรับเปลี่ยนเรื่องภาพได้ดีกว่า
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/24.jpg")
cv2.imshow("Output",img)

#แปลงจาก BGR เป็น RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()