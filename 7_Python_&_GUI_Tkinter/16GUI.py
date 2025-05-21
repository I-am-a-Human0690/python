from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk()
root.title("My GUI")

#กำหนดขนาดหน้าจอและตำแหน่ง 
root.geometry("500x500+200+200")#สูง*ยาว+(ตำแหน่งหน้าจอ)x+y

def selectColor():
    color = askcolor() #เก็บสีที่เลือกไว้ในตัวแปร
    myLanel = Label(text="hello",fg=color[1]).pack()#color[1] ชุดตัวเลขฐาน16 จากที่เลือก
    print(color)
def selectFile():
    fileopen = askopenfilename()#เก็บไฟล์ที่เลือกไว้ในตัวแปร
    print(fileopen)
    filecontent = open(fileopen,encoding="utf-8") 
    myLabel = Label(text=filecontent.read()).pack() 

btn1 = Button(text="เลือกสี",command=selectColor).pack()
btn2 = Button(text="เลือกไฟล์",command=selectFile).pack()

root.mainloop()
