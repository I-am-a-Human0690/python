import cv2

#แค่แสดงให้ดูเฉยๆไม่เกี่ยว
def display(value):
    #print(value)
    pass

#สร้างหน้าตาง
cv2.namedWindow("Output")

#สร้าง Tracker หน้าต่างที่ให้เราปรับค่าสี    #128 = min 255=Max #ชื่อต้องตรงกันOutput
cv2.createTrackbar("value","Output",128,255,display)

while True :
    #เรียกและทำให้ภาพเป็นสีเทา
    gray_img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/34.jpg",0)
    #ดึงค่าจาก Tracker #ดูหลักการทำงานได้ที่ 28
    thresh_value = cv2.getTrackbarPos("value","Output")
    #thresh เก็บค่าจุดแบ่ง                      #i ค่าจุดแบ่ง 255ค่า Max
    #THRESH_BINARY อื่นๆอยู่ที่#33 ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 255 ที่เหลือเป็น 0
    thresh, result = cv2.threshold(gray_img,thresh_value,255,cv2.THRESH_BINARY)
    if cv2.waitKey(1) & 0xFF==ord("e"):
        break
    cv2.imshow("Output",result)

cv2.destroyAllWindows()