#โปรแกรมบัญชีธนาคาร
#data
account={"นายA":5000,"นายB":0}
def getbalance():
    print("ยอดเงินคงเหลือในบัญชี : ",account)

def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนตัวเลขเท่านั้นนะครับ")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเช้าบัญชี นายA : ",money)
    account["นายA"]+=money

def withdraw(money):
    if not type(money) is int:
        raise Exception("ต้องป้อนตัวเลขเท่านั้นนะครับ")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ถอนเงินบัญชี นายA : ",money)
    account["นายA"]-=money

def transferw(money):
    if not type(money) is int:
        raise Exception("ต้องป้อนตัวเลขเท่านั้นนะครับ")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินไม่เพียงพอ")
    print("โอนเงินไปที่บัญชี นายB : ",money)
    account["นายA"]-=money
    account["นายB"]+=money

try:
    getbalance()
    deposit(1000)
    getbalance()
    withdraw(500)
    getbalance()
    transferw(2000)
    getbalance()
except Exception as c:
    print(c)