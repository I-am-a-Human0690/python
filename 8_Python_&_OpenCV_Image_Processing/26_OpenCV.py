#ตรวจจับดวงตาและใบหน้า
import cv2

#อ่านภาพ
img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/24.jpg")

#อ่านไฟล์ xml #อ่านไฟล์สำหรับ classification 
#สำหรับตรวจจับใบหน้าและดวงตา #https://github.com/opencv/opencv/tree/master/data/haarcascades #ยังมีสำหรับอื่นๆเช่นยิ้ม
face_cascade = cv2.CascadeClassifier("Python/8_Python_&_OpenCV_Image_Processing/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Python/8_Python_&_OpenCV_Image_Processing/haarcascade_eye_tree_eyeglasses.xml")

#ทำให้เป็น ภาพ grayscale ภาพเทา เพื่อใช้ในขั้นตอน #การตรวจจับใบหน้าและดวงตา
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ตรวจจับใบหน้า
face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)

#ตรวจจับดวงตา
eye_detect = eye_cascade.detectMultiScale(gray_img,1.1,4)

#แสดงตำแหน่งที่เจอ
#x,y ตำแหน่งหัวมุมซ้าย x+w,y+h ตำแหน่งหัวมุมขาวล่าง เพื่อวาดเป็นสี่เหลี่ยม
for (x,y,w,h) in face_detect:
    # rectangle(ภาพ , มุมที่ 1 บนซ้าย (x,y) , มุมที่ 2 ล่างขวา (x,y) , สี (RGB) , ความหนา)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for (ex,ey,ew,eh) in eye_detect:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)

#แสดงภาพ
cv2.imshow("Original",img)
#รอจนกว่าเราจะปิดเอง
cv2.waitKey(0)
#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()