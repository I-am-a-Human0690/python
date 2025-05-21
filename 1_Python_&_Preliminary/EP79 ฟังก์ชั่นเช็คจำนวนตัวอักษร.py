#หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่
def checkstring(message):
    a={"UPPER":0,"LOWER":0}
    for i in message:
        if i.isupper():
            a["UPPER"]+=1
        elif i.islower():
            a["LOWER"]+=1
        else:
            pass
    return a
x=input(":")
y=checkstring(x)
print(y)
