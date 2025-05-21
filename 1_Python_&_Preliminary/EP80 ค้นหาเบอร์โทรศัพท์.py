#แจ้งเหตุด่วน
data={"191":"แจ้งเหตุด่วน","1668":"รถโรงพยาบาล","1447":"รถดับเพลิง"}
def a(a):
    for key , value in data.items():
        if value == a:
            print(key)
        else :
            print("ไม่มีข้อมูล")
            return
b=input(":")
a(b)
