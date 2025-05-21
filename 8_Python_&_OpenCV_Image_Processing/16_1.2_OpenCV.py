import cv2
import datetime
cap = cv2.VideoCapture("python/8_Python_&_OpenCV_Image_Processing/2023-04-07 16-09-41.mkv")#เปิดวิดีโอ

while (cap.isOpened):
    #Check = True False มีภาพหรือไม่
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame

    if check == True:#มีเพื่อ Frame สุดท้ายหลังจากวิดีโอจบ check จะเป็น False
        currentDate = str(datetime.datetime.now()) #เวลา ณ ตอนนั้น

        # puttext(ภาพ , ข้อความ , พิกัดที่จะแสดงข้อความ (x,y) , font(ใส่เป็นรหัสก็ได้) , ขนานข้อความ , สี (RGB) , ความหนา) 
        cv2.putText(frame , currentDate , (10,30), cv2.FONT_HERSHEY_SIMPLEX ,0.8 , (255,0,0) , 2)
        if cv2.waitKey(0) & 0xFF == ord("e"): #วิดีโอจะช้าหรือเร็วขึ้นอยู่กับ cv2.waitKey(1) รอ 30 มิลลิวินาทีก่อน # 0 คือรอไปเลื่อยๆ
        #cv2.waitKey(30) & จำเป็น คือ รอ 30 มิลลิวินาที ว่าผู้ใช้จะกด e  ยิ่งตั้งเวลานานวิดีโอยิ่งช้า
            print("testwaitKey2")
            break
        print("testwaitKey")
    else:
        break
    cv2.imshow('output',frame)

cap.release()
cv2.destroyAllWindows()

'''
if cv2.waitKey(0) & 0xFF == ord("e") หากมีจะทำงานบรรทัดถัดไป โดยไม่ต้องรอให้ผู้ใช้กดแป้นพิมพ์ ถึงจะไปบรรทัดถัดไป 
เฉพาะ waitKey(0) อย่างอื่นเช่น waitKey(10000) จะต้องรอให้ครบเวลาถึงจะทำบรรทัดถัดไป
0xFF == ord("e") ถ้ากดอย่างอื่นที่ไม่ใช้ e ก็จะเป็น flase ลูปก็จะทำงานรอบถัดไป
'''
