#โอนเงิน
#Exeption
#else: ถ้าไม่มีข้อผิดพลาดก้จะทำงาน
try:
    a=int(input(":"))
    b=int(input(":"))
    c=a/b
    print(c)
    print("โอนเงิน")
except Exception as e:
    print(e)
else:
    print("โอนเงินสำเร็จ")