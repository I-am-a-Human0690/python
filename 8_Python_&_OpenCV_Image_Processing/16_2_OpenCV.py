import cv2
import datetime
cap = cv2.VideoCapture(0)#เปิดกล้อง

while (cap.isOpened):
    #Check = True False มีภาพหรือไม่
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame

    if check == True:#มีเพื่อ Frame สุดท้ายหลังจากวิดีโอจบ check จะเป็น False
        currentDate = str(datetime.datetime.now()) #เวลา ณ ตอนนั้น

        # puttext(ภาพ , ข้อความ , พิกัดที่จะแสดงข้อความ (x,y) , font(ใส่เป็นรหัสก็ได้) , ขนานข้อความ , สี (RGB) , ความหนา) 
        cv2.putText(frame , currentDate , (10,30), cv2.FONT_HERSHEY_SIMPLEX ,0.8 , (255,0,0) , 2)
        cv2.imshow('output',frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): #วิดีโอจะช้าหรือเร็วขึ้นอยู่กับ cv2.waitKey(1) # 0 คือรอไปเลื่อยๆ
        #cv2.waitKey(1) & จำเป็น คือ รอ 1 มิลลิวินาที ว่าผู้ใช้จะกด e  ยิ่งตั้งเวลานานภาพยิ่งกระตุก
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

#ถ้าต้องการให้แสดงเวลาในบันทึกวิดีโอก็ทำได้
