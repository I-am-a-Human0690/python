#การใช้งาน Adaptive Threshold #ดูรูปจาก 36
import cv2 
img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/37.jpg",0)

#แบบเดิม
thresh,th1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
#คำนวณค่าเฉลี่ยรอบๆ BlockSize แล้วหักจากค่า C 255=max 3 = BlockSize(3*3) 1 = ค่า C
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
#คำนวณค่าเฉลี่ยรอบๆ BlockSize แล้วอ้างอิงทำการทำงานกับฟังก็ชั่น Gaussian และค่า 
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)
cv2.imshow("ก่อนปรับ",img)
cv2.imshow("THRESH",th1)
cv2.imshow("MEAN",th2)
cv2.imshow("GAUSSIAN",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()