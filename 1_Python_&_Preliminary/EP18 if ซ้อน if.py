#if ซ่อน if
age=int(input("กระรุณากรอกอายุของท่าน "))
if age>=16:#เช็คเงื่อนไขนี้ก่อน
    if age==16:#จึงเช็คเงื่อนไขข้างใน
        print("ม.4")
    elif age==16:
    #elif age==17:
        print("ม.5") #จะไม่ทำบรรทัดนี้
    elif age==18:
        print("ม.6")
    else:
        print("มหาลัยหรือสูงกว่า")
else :#eles ใส่เงื่อนไขไม่ได้
    if age==13:
        print("ม.1")
    elif age==14:
        print("ม.2")
    elif age==15:
        print("ม.3")
    else:
        print("ประถม")
print("จบโปรแกรม")