fw=open('Python/1_Python_&_Preliminary/EP93.1.txt',"w",encoding="utf-8")# W เป็นการสร้างไฟล์เพื่อเขียน  และจะเขียนทับิันเก่า
fw.write("wwwwq")
fw.write("2wwwwq")
fw.writelines("qqqqq\nฟ")
fw.writelines("3")
fw.close

fr=open('Python/1_Python_&_Preliminary/EP93.1.txt',"r",encoding="utf-8")
print(fr.read())
fr.close

fr=open('Python/1_Python_&_Preliminary/EP93.1.txt',"r",encoding="utf-8")
a=fr.readlines()
for i in a: #ตัวแปรที่เก็บไว้ใน i เป็น str
    print(i)

# for i in fr: #แบบนี้ก็ได้
#     print(i)