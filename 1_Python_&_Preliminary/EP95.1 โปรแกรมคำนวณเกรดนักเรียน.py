#โปรแกรมเกรด #ไม่ระบุตัวแปร None 
# try:
#     fw=open("EP95.2.txt","a",encoding="utf-8")
#     while True:
#         studentid=input("ป้อนรหัสนักเรียน :")
#         if studentid == "asd":
#             break
#         score=input("ป้อนคะแนนสอบ")
#         fw.writelines(studentid+"\t"+score+"\n")
#     fw.close()
# except Exception as e:
#     print(e)
#หลังจากป้อนเสร็๗
fr=open("EP95.2.txt","r",encoding="utf-8")
fe=open("EP95.3.txt","a",encoding="utf-8")
grade=None
for line in fr.readlines():
    score=line[-3:].strip()
    studentid=line[:3].strip()
    score=int(score)
    if score>=80:
        grade="A"
    elif score>=70 and score<80:
        grade="B"
    elif score>=60 and score<70:
        grade="c" 
    elif score>=50 and score<60:
        grade="D" 
    else:
        grade="F"
    fe.writelines(studentid+"\t"+str(score)+"\t"+str(grade)+"\n")
