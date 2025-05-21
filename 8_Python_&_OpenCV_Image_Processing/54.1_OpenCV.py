#Motion Detection
import cv2 
cap = cv2.VideoCapture("Python/8_Python_&_OpenCV_Image_Processing/54.mp4")
check , frame1 = cap.read()#รับภาพจากกล้อง(จากวิดีโอ) Frame ต่อ Frame
check , frame2 = cap.read()
while (cap.isOpened()):
    #Check = True False มีภาพหรือไม่
    if check == True :
        #ฟังก์ชัน cv2.absdiff() สามารถใช้เป็นขั้นตอนเบื้องต้นในการระบุการเคลื่อนไหวของวัตถุในภาพได้
        motiondiff= cv2.absdiff(frame1,frame2)
        #cv2.imshow("Output",frame1)
        cv2.imshow("Output",motiondiff)
        frame1=frame2
        check,frame2 = cap.read()
        if cv2.waitKey(30) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()