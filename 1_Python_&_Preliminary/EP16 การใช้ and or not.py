age=int(input("กระรุณากรอกชื่อของท่าน "))
if age>=15 and age<=19:
    print("ท่านอยู่ในวัยรุ่น")
elif age>=20 and age<=29:
    print("ท่านอยู่ในวัยหนุ่มสาว")
elif age>=30 and age<=49:
    print("ท่านอยู่ในวัยผู้ใหญ่")
elif age>=50:
    print("ท่านอยู่ในวัยชรา")
else:
    print("ท่านอยู่ในวัยเด็ก")
print("จบโปรแกรม")