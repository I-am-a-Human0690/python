import cv2


img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png') #0=ภาพเทา, 1=ภาพสี, -1=?

#resize
imgresize = cv2.resize(img,(800,500))

#วาดสี่เหลี่ยม
# rectangle(ภาพ , มุมที่ 1 บนซ้าย (x,y) , มุมที่ 2 ล่างขวา (x,y) , สี (RGB) , ความหนา)
#cv2.rectangle(imgresize,(100,100),(400,400),(0,0,255),10) 
cv2.rectangle(imgresize,(100,100),(400,400),(0,0,255),-1) #ข้างในทึม



#แสดงภาพ
cv2.imshow('ชื่อภาพ',imgresize)

#แสดงจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

