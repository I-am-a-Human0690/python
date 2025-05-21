import cv2

cap = cv2.VideoCapture(0)#กล้อง
fourcc = cv2.VideoWriter_fourcc(*'XVID')#รูปแบบวิดีโอ

#avi นามสกุลของไฟล์วิดีโอ, รูปแบบวิดีโอ, เฟมเรต, ขนาด
result = cv2.VideoWriter('python/8_Python_&_OpenCV_Image_Processing/11.avi',fourcc,20.0,(640,480))

while (cap.isOpened):
    #Check = True False มีภาพหรือไม่
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame

    if check == True:#มีเพื่อ Frame สุดท้ายหลังจากวิดีโอจบ check จะเป็น False
        cv2.imshow('output',frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): #วิดีโอจะช้าหรือเร็วขึ้นอยู่กับ cv2.waitKey(1)
        #cv2.waitKey(1) & จำเป็น คือ รอ 1 มิลลิวินาที ว่าผู้ใช้จะกด e หรือไม่ก่อนค่อยแสดงภาพรอบถัดไป ยิ่งตั้งเวลานานภาพยิ่งกระตุก
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

'''
H.264: เป็นรูปแบบที่เป็นที่นิยมมากในการบีบอัดวิดีโอ HD และรองรับการสตรีมวิดีโอออนไลน์.

MP4V: สำหรับการบีบอัดวิดีโอในรูปแบบ MP4.

MJPG: สำหรับการบีบอัดวิดีโอในรูปแบบ Motion JPEG.

DIVX: รูปแบบที่ได้รับความนิยมในอดีตสำหรับการบีบอัดวิดีโอ.

และอื่น ๆ อีกมากมาย...
'''
