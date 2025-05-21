#Exeption
#สร้าง Exeption ด้วย raise
while True:
    try:
        c=input("ป้อนชื่อ : ")
        if c == "ก" or "a":
            raise Exception("มีชื่อนี้ในระบบแล้ว")
        a=int(input(":"))
        b=int(input(":"))
        if a == 0 and b == 0:
            break
        if a<0 or b>0:
            raise Exception("มีชื่อนี้ในระบบแล้ว")
        c=a/b
        print(c)
        print("โอนเงิน")
    except Exception as e:
        print(e)
    finally:
        print("ทำงานต่อไป")