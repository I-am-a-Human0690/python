import cv2


img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png') #0=ภาพเทา, 1=ภาพสี, -1=?

#resize
imgresize = cv2.resize(img,(800,500))

#Drawing Functions
#https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html

#วาดข้อความบนภาพ
# puttext(ภาพ , ข้อความ , พิกัดที่จะแสดงข้อความ (x,y) , font(ใส่เป็นรหัสก็ได้) , ขนานข้อความ , สี (RGB) , ความหนา) 
cv2.putText(imgresize, "text" , (300,300), cv2.FONT_HERSHEY_SIMPLEX ,2.5 , (255,0,0) , cv2.LINE_8) #ข้อความภาษาไทยไม่ได้
#cv2.putText(imgresize, "text" , (300,300), 0 ,2.5 , (255,0,0), 5 ) #ใส่เป็นรหัส



#แสดงภาพ
cv2.imshow('ชื่อภาพ',imgresize)

#แสดงจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

