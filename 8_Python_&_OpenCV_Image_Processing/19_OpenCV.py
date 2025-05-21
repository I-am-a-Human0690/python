import cv2
import numpy

img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/18.png')
#resize
imgresize = cv2.resize(img,(800,700))

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
                        #LBUTTONDOWN, RBUTTONDOWN  
                        #cv2.EVENT_LBUTTONDOWN คลิก
                        #cv2.EVENT_LBUTTONUP คลิกแล้วปล่อย
        red = imgresize[y,x,2]
        green = imgresize[y,x,1]
        blue = imgresize[y,x,0]
        imgcolor = numpy.zeros([300,300,3],numpy.uint8) # 300*300,3มิติ #,numpy.uint8 ไม่มีก็ได้
        #print(imgcolor)
        imgcolor[:] = [blue, green, red] #จำเป็นต้องเรียง bgr
        cv2.imshow("result", imgcolor)

#แสดงภาพ
cv2.imshow('output',imgresize)

#ทำงานกับ Mouse
cv2.setMouseCallback("output", clickPosition)

#รอจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()
