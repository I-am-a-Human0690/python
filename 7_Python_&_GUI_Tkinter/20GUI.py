from tkinter import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

def showChoice():
    if language1.get() == 1:
        Label(text="เลือกภาษา Pthon").pack(anchor=W)
    if language2.get() == 1:
        Label(text="เลือกภาษา C").pack(anchor=W)
    if language3.get() == 1:
        Label(text="เลือกภาษา PHP").pack(anchor=W)
        
    print(language1.get(),language2.get(),language3.get())

#0 ไม่ได้เลือกตัวเลือก 1 เลือกตัวเลือก
language1 = IntVar()
Checkbutton(text="Pyhon",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="C",variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=W)

Button(text="แสดงตัวเลือก",command=showChoice).pack(anchor=W)
root.mainloop()
