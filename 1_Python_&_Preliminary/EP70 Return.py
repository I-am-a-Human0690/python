#none
def a(x):
    if len(x)<3:
        return
    if x=="100":
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0
x=a("100")
print(x)