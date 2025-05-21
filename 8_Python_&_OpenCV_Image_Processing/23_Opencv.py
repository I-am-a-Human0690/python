import cv2

#อ่านวิดีโอ
cap = cv2.VideoCapture("Python/8_Python_&_OpenCV_Image_Processing/23.mp4")

#อ่านไฟล์สำหรับ classification 
#สำหรับตรวจจับใบหน้า #https://github.com/opencv/opencv/tree/master/data/haarcascades #ยังมีสำหรับอื่นๆเช่นยิ้ม
face_cascade=cv2.CascadeClassifier("Python/8_Python_&_OpenCV_Image_Processing/haarcascade_frontalface_default.xml")

#แสดงผลวิดีโอ
while (cap.isOpened()):
    #Check = True False มีภาพหรือไม่
    check , frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame
    if check == True :
        #ทำให้เป็น ภาพ grayscale ภาพเทา เพื่อใช้ในขั้นตอน #การตรวจจับใบหน้า
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #เก็บตำแหน่งที่เจอใบหน้า #การตรวจจับใบหน้า detectMultiScale
        face_detect = face_cascade.detectMultiScale(gray_img,1.2,3) 
        #แสดงตำแหน่งที่เจอใบหน้า
        #x,y ตำแหน่งหัวมุมซ้าย x+w,y+h ตำแหน่งหัวมุมขาวล่าง เพื่อวาดเป็นสี่เหลี่ยม
        for (x,y,w,h) in face_detect:
            # rectangle(ภาพ , มุมที่ 1 บนซ้าย (x,y) , มุมที่ 2 ล่างขวา (x,y) , สี (RGB) , ความหนา)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)
        if cv2.waitKey(30) & 0xFF == ord("e"):#วิดีโอจะช้าหรือเร็วขึ้นอยู่กับ cv2.waitKey() # 0 คือรอไปเลื่อยๆ
            #cv2.waitKey(30) & จำเป็น คือ รอ 30 มิลลิวินาที ว่าผู้ใช้จะกด e  ยิ่งตั้งเวลานานวิดีโอยิ่งช้า
            break
    else :
        break
cap.release()

#ปิดหน้าต่างทั้งหมดที่ถูกสร้างโดย cv2.imshow()
cv2.destroyAllWindows()
