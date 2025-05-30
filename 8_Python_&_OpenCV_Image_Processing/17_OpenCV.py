import cv2

img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png')
#resize
imgresize = cv2.resize(img,(800,500))

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
                        #LBUTTONDOWN, RBUTTONDOWN  
                        #cv2.EVENT_LBUTTONDOWN คลิก
                        #cv2.EVENT_LBUTTONUP คลิกแล้วปล่อย
        text = str(x)+","+str(y)
        # puttext(ภาพ , ข้อความ , พิกัดที่จะแสดงข้อความ (x,y) , font(ใส่เป็นรหัสก็ได้) , ขนานข้อความ , สี (RGB) , ความหนา) 
        cv2.putText(imgresize, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
        cv2.imshow("output", imgresize)

#แสดงภาพ
cv2.imshow('output',imgresize)

#ทำงานกับ Mouse
cv2.setMouseCallback("output", clickPosition)

#รอจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()
