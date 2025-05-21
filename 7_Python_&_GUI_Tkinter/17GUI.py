from tkinter import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

#เพิ่มตัวเลือกในโปรแกรม
language = IntVar()
Radiobutton(text="Python",variable=language,value=1).grid(row=0,column=0)
Radiobutton(text="Java",variable=language,value=2).grid(row=0,column=1)
Radiobutton(text="PHP",variable=language,value=3).grid(row=0,column=2)
Radiobutton(text="C",variable=language,value=4).grid(row=0,column=3)

root.mainloop()
