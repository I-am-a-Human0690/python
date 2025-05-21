from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

# สร้าง Menu
myMenu = Menu()
root.config(menu=myMenu)

#สร้างหน้าต่างใหม่อตนคลิก New Window
def showWindow():
    window = Tk()
    window.title("หน้าต่าง New Window")
    window.geometry("300x300+100+100")
    window.mainloop

def aboutProgrogram():
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรม","ผู้พัฒนานายสิทธิกร")

#เพิ่ม Menu ย่อย (Menu Item)
menuitem = Menu()
menuitem.add_command(label="New Window",command=showWindow)
menuitem.add_command(label="Open")
menuitem.add_command(label="Save")
menuitem.add_command(label="About",command=aboutProgrogram)
menuitem.add_command(label="Exit")

# เพิ่ม Menu
myMenu.add_cascade(label="File",menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()
