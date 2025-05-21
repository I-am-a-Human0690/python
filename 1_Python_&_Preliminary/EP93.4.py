#เขียนไฟล์ต่อโดยไม่ทับ
fa=open('./Python/1Python_&_Preliminary/EP93.2.txt',"a",encoding="utf-8")
fa.writelines("\nagjfy") 
fa.close

# fa=open("EP93.2.txt","r",encoding="utf-8")
# print(fa.read())
# fa.close

#ชื่อตัวแปรไม่เหมือนเดิม จะไม่แสดงที่เขียนล่าสุด
# fr=open("EP93.2.txt","r",encoding="utf-8")
# print(fa.read())
# fr.close