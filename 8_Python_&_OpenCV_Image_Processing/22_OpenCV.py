import cv2

#อ่านภาพ
img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/22.jpg")

#อ่านไฟล์สำหรับ classification 
#สำหรับตรวจจับใบหน้า #https://github.com/opencv/opencv/tree/master/data/haarcascades #ยังมีสำหรับอื่นๆเช่นยิ้ม
face_cascade=cv2.CascadeClassifier("Python/8_Python_&_OpenCV_Image_Processing/haarcascade_frontalface_default.xml")


#ทำให้เป็น ภาพ grayscale ภาพเทา เพื่อใช้ในขั้นตอน #จำแนกใบหน้า
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#จำแนกใบหน้า #2 ค่านี้มีผลต่อการตรวจจับใบหน้า
scaleFactor = 1.1   #ค่าเริ่มต้นที่ 1.1  
#>1 เช่น1.1 คือแกนแต่ละรอบจะลดขนาดภาพทีละ 10% <1 เช่น 0.9 คือลดขนาดภาพทีละ 10% #แต่อันนี้ไม่สามารถน้อยกว่า 1 ได้
minNeighber = 3     #ค่าเริ่มต้นที่ 3 
#ถ้าเจอจุดนี้เป็นใบหน้า >=3 นับว่าเป็นใบหน้าเดียวตีกรอบครั้งเดียว #ลองปรับเป็น 0


#ไม่กำหนด scaleFactor,minNeighber ก็ได้เพราะมีค่า Defalt แล้ว
#เก็บตำแหน่งที่เจอใบหน้า #การตรวจจับใบหน้า detectMultiScale
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber) 


#แสดงตำแหน่งที่เจอใบหน้า
#x,y ตำแหน่งหัวมุมซ้าย x+w,y+h ตำแหน่งหัวมุมขาวล่าง เพื่อวาดเป็นสี่เหลี่ยม
for(x,y,w,h) in face_detect:
    # rectangle(ภาพ , มุมที่ 1 บนซ้าย (x,y) , มุมที่ 2 ล่างขวา (x,y) , สี (RGB) , ความหนา)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2) #hickness= ไม่ใส่ก็ได้

#แสดงภาพ
cv2.imshow("Original",img)

#รอจนกว่าจะปิดเอง
cv2.waitKey(0)

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()
