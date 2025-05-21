from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

def selectColor():
    color = askcolor() #เก็บสีที่เลือกไว้ในตัวแปร
    myLanel = Label(text="hello",fg=color[1]).pack()#color[1] ชุดตัวเลขฐาน16 จากที่เลือก
    print(color)
    print(color[0])
    print(color[1])

btn = Button(text="เลือกสี",command=selectColor).pack()

root.mainloop()
