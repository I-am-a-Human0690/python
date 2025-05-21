from tkinter import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

# สร้าง Menu
myMenu = Menu()
root.config(menu=myMenu)

#เพิ่ม Menu ย่อย (Menu Item)
menuitem = Menu()
menuitem.add_command(label="New File")
menuitem.add_command(label="Open")
menuitem.add_command(label="Save")
menuitem.add_command(label="Exit")

# เพิ่ม Menu
myMenu.add_cascade(label="Menu1",menu=menuitem)
myMenu.add_cascade(label="Menu2")
myMenu.add_cascade(label="Menu3")

root.mainloop()
