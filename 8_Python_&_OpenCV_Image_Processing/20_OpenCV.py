import cv2
import numpy

#img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/18.png')
#resize
#imgresize = cv2.resize(img,(800,700))

img2 = numpy.zeros([600,600,3])# 600*600,3มิติ 
points = []

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
                        #LBUTTONDOWN, RBUTTONDOWN  
                        #cv2.EVENT_LBUTTONDOWN คลิก
                        #cv2.EVENT_LBUTTONUP คลิกแล้วปล่อย
        # circle(ภาพ , จุดศูนย์กลาง (x,y) , รัศมี , สี (RGB) , ความหนา) วงกลมจุดที่คลิก
        cv2.circle(img2, (x,y), 10, (0,0,255),5)
        points.append((x,y))
        if len(points) >= 2:
            # line(ภาพ , จุดเริ่ม (x,y) , จุดสุดท้าย (x,y) , สี (RGB) , ความหนา)แบบไม่มีหัวลูกศร
            cv2.line(img2,points[-2],points[-1],(0,255,0),5)
        cv2.imshow("output", img2)

#แสดงภาพ
cv2.imshow('output',img2)

#ทำงานกับ Mouse
cv2.setMouseCallback("output", clickPosition)

#รอจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()
