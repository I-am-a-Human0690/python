import cv2
import numpy

img=cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/21.jpg') #ในลูปนอกรูปก็ได้
img=cv2.resize(img,(400,400))

while True :

    #ช่วงของสี BGR
    lower = numpy.array([5,111,10])
    upper = numpy.array([124,255,133])

    mask=cv2.inRange(img,lower,upper)#รูปมี pixel ไหนที่อยู่ในช่วงสีที่เรากำหนดบ้าง สีขาวคือช่วงสี สีดำคือไม่อยู่ในช่วง
    result = cv2.bitwise_and(img,img,mask=mask) #นำสีจากรูปต้นฉบับไปใส่ในสีขาว
    if cv2.waitKey(0) & 0xFF == ord("e"): #รอ 0 มิลลิวินาที คือรอไปเลื่อยๆ
        print("testwaitKey2")
        break
    cv2.imshow("Original",img)
    cv2. imshow("Mask" ,mask)
    cv2.imshow("Result",result)
    print("testwaitKey")


#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()

'''
if cv2.waitKey(0) & 0xFF == ord("e") หากมีจะทำงานบรรทัดถัดไป โดยไม่ต้องรอให้ผู้ใช้กดแป้นพิมพ์ ถึงจะไปบรรทัดถัดไป 
เฉพาะ waitKey(0) อย่างอื่นเช่น waitKey(10000) จะต้องรอให้ครบเวลาถึงจะทำบรรทัดถัดไป
0xFF == ord("e") ถ้ากดอย่างอื่นที่ไม่ใช้ e ก็จะเป็น flase ลูปก็จะทำงานรอบถัดไป
'''