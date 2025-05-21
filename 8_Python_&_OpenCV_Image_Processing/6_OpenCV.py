import cv2


img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png',0) #0=ภาพเทา, 1=ภาพสี, -1=?

#resize
imgresize = cv2.resize(img,(400,400))

#แสดงภาพ
cv2.imshow('ชื่อภาพ',imgresize)


#รอ 5 วิแล้วปิด
cv2.waitKey(delay=5000)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

