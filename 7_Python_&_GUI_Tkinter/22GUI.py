from tkinter import *
root = Tk()
root.title("โปรแกรมคำนวนพื้นที่")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

# พื้นที่งวกลม = πr2 โดยให้ค่า π มีค่า 3.14
Label(text="รัศมี",font=30).grid(row=0,sticky=W)
radius = IntVar()
et1 = Entry(width=30,textvariable=radius,font=30)
et1.grid(row=0,column=1)

Label(text="พื้นที่วงกลม",font=30).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)

def calculate():
    r = radius.get()
    area = 3.14 *r*r
    et2.insert(0,area)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

btn = Button(text="คำนวน",command=calculate).grid(row=2,column=1,sticky=W)
btn2 = Button(text="ล้าง",command=calculate).grid(row=2,column=1,sticky=E)
root.mainloop()
