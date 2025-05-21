#Exeption
#ใช้ร่วมกับ loop while
while True:
    try:
        a=int(input(":"))
        b=int(input(":"))
        if a == 0 and b == 0:
            break
        c=a/b
        print(c)
        print("โอนเงิน")
    except Exception as e:
        print(e)
    finally:
        print("ทำงานต่อไป")