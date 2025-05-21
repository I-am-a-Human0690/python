#การสร้าง TrackBar เบื้องต้น
import cv2
import numpy as np

img =np.zeros((400,400,3),np.uint8) #400*400 3มิติ ค่าเริ่มต้นคือ 0 สีดำ

#สร้างหน้าตาง
cv2.namedWindow("Color Trackbar")

#แค่แสดงให้ดูเฉยๆไม่เกี่ยว
def display(value):
    print(value)

#เริ่มต้นสร้าง Tracker หน้าต่างที่ให้เราปรับค่าสี    #0 = min 255=Max #ชื่อต้องตรงกันColor Trackbar
cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)

while True:
    #ถ้ายากให้แยกหน้าต่างให้ใช้ชื่อใหม่
    #cv2.imshow("Color Trackbar2",img)
    cv2.imshow("Color Trackbar",img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    #ตึงค่าจาก Trackber
    blue = cv2.getTrackbarPos("B","Color Trackbar")
    green = cv2.getTrackbarPos("G","Color Trackbar")
    red = cv2.getTrackbarPos("R","Color Trackbar")
    img[:] = [blue,green,red]
    #print("0") testดูการทำงาน

#cv2.waitKey(1000)#กด e แล้วสีจะไม่เปลี่ยนแล้ว แต่Trackbarจะยังทำงานจนกว่าจะครบเวลาแล้วจบโปรแกรม   testดูการทำงานก
cv2.destroyAllWindows()