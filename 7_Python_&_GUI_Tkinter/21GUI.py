from tkinter import *
root = Tk()
root.title("Data Entry")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

Label(text="ชื่อ").grid(row=0)
Label(text="นามสกุล").grid(row=1)
Label(text="เบอร์โทร").grid(row=2)

et1=Entry()
et1.grid(row=0,column=1)
et1.insert(0,"สิทธิกร")

et2=Entry()
et2.grid(row=1,column=1)
et2.insert(0,"ชมภูพื้น")

et3=Entry()
et3.grid(row=2,column=1)
et3.insert(0,"0953864469")

def deleteText():
    et1.delete(0,END) #.delete(index เริ่ม,index จบ)
    et2.delete(0,END)
    et3.delete(0,END)

button = Button(text="ล้างข้อมูล",command=deleteText).grid(row=3,column=1)

root.mainloop()
