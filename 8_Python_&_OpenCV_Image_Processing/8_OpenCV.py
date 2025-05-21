import cv2

cap = cv2.VideoCapture(0)#เปิดกล้อง


#Check = True False มีภาพหรือไม่
while (True):
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame
    cv2.imshow('output',frame)

    if cv2.waitKey(1) & 0xFF == ord("e"): 
        #cv2.waitKey(1) & จำเป็น คือ รอ 1 มิลลิวินาที ว่าผู้ใช้จะกด e หรือไม่ก่อนค่อยแสดงภาพรอบถัดไป ยิ่งตั้งเวลานานภาพยิ่งกระตุก
        break

cap.release()
cv2.destroyAllWindows()

'''cap.release() เป็นฟังก์ชันที่ใช้สำหรับปล่อยทรัพยากรของกล้องหรือวิดีโอที่ถูกเปิดด้วย 
OpenCV หลังจากที่เราใช้งานเสร็จสิ้นแล้ว เพื่อให้แน่ใจว่าทรัพยากรนั้นถูกปล่อยและไม่มีการค้างอยู่'''