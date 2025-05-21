from tkinter import *
root = Tk()
root.title("My GUI")
#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

#ใส่ข้อความ การจัดเรียง
#.place/.grid ใช้ด้วยกันได้แต่เลือกสักอย่าง  .place/.pack() ใช้ด้วยกันได้   .place/.grid ใช้ด้วยกันไม่ได้ แนะนำเลือกใช้ .grid
myLabe1 = Label(root,text="Hello world",fg="black",font=40,bg="yellow").place(x=100,y=100)
# myLabe2 = Label(root,text="Hello world",fg="black",font=40,bg="yellow").grid(row=70,column=70)
myLabe3 = Label(root,text="Hello world",fg="black",font=40,bg="yellow").pack()

root.mainloop()
