from tkinter import *
root = Tk()
root.title("My GUI")
#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

#ใส่ข้อความ การจัดเรียง
myLabe2 = Label(root,text="Hello world",fg="black",font=40,bg="yellow").pack()

#command
def showMessage():
    Label(root,text="Hello",fg="black",font=40,bg="yellow").pack()

#ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",bg="red",command=showMessage).pack()

root.mainloop()
