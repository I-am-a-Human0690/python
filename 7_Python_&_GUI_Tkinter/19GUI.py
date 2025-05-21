from tkinter import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

def showChoice():
    print(language1.get(),language2.get(),language3.get())

#0 ไม่ได้เลือกตัวเลือก 1 เลือกตัวเลือก
language1 = IntVar()
Checkbutton(text="Pyhon",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="C",variable=language2).pack(anchor=NW)
language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=E)

Button(text="แสดงตัวเลือก",command=showChoice).pack(anchor=S)
root.mainloop()
