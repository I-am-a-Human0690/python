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

#กล่องข้อความ
txt=StringVar()
mytxt=Entry(root,textvariable=txt).pack()

#ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",bg="red",command=showMessage).pack()

root.mainloop()
