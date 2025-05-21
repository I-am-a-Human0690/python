import cv2


img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png') #0=ภาพเทา, 1=ภาพสี, -1=?

#resize
imgresize = cv2.resize(img,(800,500))

#วาดเส้นตรง
# line(ภาพ , จุดเริ่ม (x,y) , จุดสุดท้าย (x,y) , สี (RGB) , ความหนา)
#cv2.line(imgresize,(100,100),(500,200),(255,0,0),10) #แบบปกติ
cv2.arrowedLine(imgresize,(100,100),(500,200),(255,0,0),10) #แบบมีหัวลูกศร
cv2.arrowedLine(imgresize,(100,100),(400,200),(0,255,0),10) #มีได้หลายเส้น


#แสดงภาพ
cv2.imshow('ชื่อภาพ',imgresize)

#แสดงจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

