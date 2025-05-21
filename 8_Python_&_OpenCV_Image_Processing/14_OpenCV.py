import cv2


img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png') #0=ภาพเทา, 1=ภาพสี, -1=?

#resize
imgresize = cv2.resize(img,(800,500))

#วาดวงกลม
# circle(ภาพ , จุดศูนย์กลาง (x,y) , รัศมี , สี (RGB) , ความหนา) 
#cv2.circle(imgresize,(300,300),50,(0,0,255),5) 
cv2.circle(imgresize,(300,300),50,(0,0,255),-1)  # ข้างในทึม



#แสดงภาพ
cv2.imshow('ชื่อภาพ',imgresize)

#แสดงจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

