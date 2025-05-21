#Motion Detection
import cv2 
cap = cv2.VideoCapture("Python/8_Python_&_OpenCV_Image_Processing/54.mp4")
check , frame1 = cap.read()#รับภาพจากกล้อง(จากวิดีโอ) Frame ต่อ Frame
check , frame2 = cap.read()
while (cap.isOpened()):
    #Check = True False มีภาพหรือไม่
    if check == True :
        #ฟังก์ชัน cv2.absdiff() สามารถใช้เป็นขั้นตอนเบื้องต้นในการระบุการเคลื่อนไหวของวัตถุในภาพได้
        #เพื่อให้หาเส้นขอบได้ง่ายขึ้น
        motiondiff= cv2.absdiff(frame1,frame2)

        #ทำให้ภาพเป็นสีเทา
        gray=cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)

        #Gaussian Filter #ลด noise ยิ่งตัวกรองใหญ่ยิ่ง ลด noise เยอะแต่ภาพยิ่งเบลอ #ในวิดีโอไม่ค่อยมี noise ไม่ใช้ก็ได้
        #ขยายเส้นรอบวัตุถุ #คำอธิบายใน 54.1.png 
        blur = cv2.GaussianBlur(gray,(5,5),0)#48

        #thresh ค่าจุดแบ่ง                   #15 ค่าจุดแบ่ง 255ค่า Max
        #ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 255 ที่เหลือเป็น 0  #ทำให้เป็นภาพขาวดำ #เพื่อใช้ใน #การขยายภาพ
        thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)#33

        #การขยายภาพ ทำเพื่อเติมเส้นที่ขาด #39
        dilation = cv2.dilate(result,None,iterations=3)

        #หาเส้นรอบวัตถุ จากภาพขาวดำที่ทำการขยายและต่อเส้นแล้ว
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#53

        #เอาเส้นใสในรูป
        cv2.drawContours(frame1,contours,-1,(0,255,0),2)#53
        
        cv2.imshow("Output",frame1)
        frame1=frame2
        check,frame2 = cap.read()
        if cv2.waitKey(30) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()