#เส้นเค้าโครง (Contour)
#สามารถใช้ ฟังชั่นในเรื่อง threshต่างๆ (#การขยายภาพ, #การกร่อนภาพ, #opening ช่วยลบ noise,
 #closing ช่วยในการเติมเต็มจุดข้อมูลที่ขาดหาย) มาช่วยได้ #31
import cv2 

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/34.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh,result = cv2.threshold(gray,215,255,cv2.THRESH_BINARY) #31

contours,hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#print(contours)
print(len(contours))

cv2.drawContours(img,contours,-1,(0,255,0),2)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()