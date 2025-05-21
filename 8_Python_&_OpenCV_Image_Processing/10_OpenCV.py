import cv2

cap = cv2.VideoCapture("python/8_Python_&_OpenCV_Image_Processing/2023-04-07 16-09-41.mkv")#เปิดวิดีโอ

while (cap.isOpened):
    #Check = True False มีภาพหรือไม่
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame

    if check == True:#มีเพื่อ Frame สุดท้ายหลังจากวิดีโอจบ check จะเป็น False
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#แปลง Frame จาก สีเป็นเทา
        cv2.imshow('output',gray)
        if cv2.waitKey(1) & 0xFF == ord("e"): #วิดีโอจะช้าหรือเร็วขึ้นอยู่กับ cv2.waitKey(1)
        #cv2.waitKey(1) & จำเป็น คือ รอ 1 มิลลิวินาที ว่าผู้ใช้จะกด e หรือไม่ก่อนค่อยแสดงภาพรอบถัดไป ยิ่งตั้งเวลานานภาพยิ่งกระตุก
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
