from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

def showChoice():
    choice = language.get()
    print(choice)
    if choice == 1:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือกภาษา Python")
    elif choice == 2:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือกภาษา Java")
    elif choice == 3:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือกภาษา PHP")
    elif choice == 4:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือกภาษา C")
        
#เพิ่มตัวเลือกในโปรแกรม
language = IntVar()
language.set(2) #ค่าเริ่มต้น
Radiobutton(text="Python",variable=language,value=1,command=showChoice).grid(row=0,column=0)
Radiobutton(text="Java",variable=language,value=2,command=showChoice).grid(row=0,column=1)
Radiobutton(text="PHP",variable=language,value=3,command=showChoice).grid(row=0,column=2)
Radiobutton(text="C",variable=language,value=4,command=showChoice).grid(row=0,column=3)
#variable=กำไว้ในตัวแปรนี้,value=เลือกแล้วจะให้เก็บเป็นอะไร

root.mainloop()
