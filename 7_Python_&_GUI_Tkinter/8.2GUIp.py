from tkinter import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

#ใส่ข้อความ การจัดเรียง
myLabe2 = Label(root,text="Hello world",fg="black",font=40,bg="yellow").pack()

#command
def showMessage():
    message = txt.get()
    Label(root,text=message,fg="black",font=40,bg="yellow").pack()
    print(message)
def openWindow():
    #หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("500x500+100+100")

#กล่องข้อความ
txt=StringVar()
mytxt=Entry(root,textvariable=txt).pack()  #Entry=กล่องใส่ข้อความ

#ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",bg="red",command=showMessage).pack()
btn1 = Button(root,text="เปิดรายงาน",fg="white",bg="red",command=openWindow).pack()

root.mainloop()
