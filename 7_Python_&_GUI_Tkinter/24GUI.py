#1 บาท = 0.026 EUR
#1 บาท = 3.486 JPY
#1 บาท = 0.031 USD
#1 บาท = 0.023 GBP

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("แปลงสกุลเงิน")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

#input
money = IntVar()
Label(text="จำนวนเงิน",padx=10,font=30).grid(row=0,column=0,sticky=W)
et1 = Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo = ttk.Combobox(width=28,font=30,textvariable=choice)
combo.grid(row=1,column=1,sticky=W)
combo["values"] = ("EUR","JPY","USD","GBP")

#output
Label(text="ผลการคำนวน",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font=30,width=30)
et2.grid(row=2,column=1)

def calculate():
    et2.delete(0,END)
    if choice.get()=="EUR":
        result = ((money.get()*0.026),"EUR")
    elif choice.get()=="JPY":
        result = ((money.get()*3.486),"JPY")
    elif choice.get()=="USD":
        result = ((money.get()*0.031),"USD")
    elif choice.get()=="GBP":
        result = ((money.get()*0.023),"GBP")
    et2.insert(0,result)

def delete():
    et1.delete(0,END)
    et2.delete(0,END)
Button(text="คำนวน",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้างค่า",font=30,width=15,command=delete).grid(row=3,column=1,sticky=E)
root.mainloop()
