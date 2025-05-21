#เจาะลึกพังชั่น string(str)
#ลบช่องว่าง
name=("  sitthikon  ")
print(name)
print(len(name))
#ลบช่องว่างซ้ายและขวา
name2=("  sitth ikon  ")
name2=name2.strip()
print(name2)
print(len(name2))
#ลบช่องว่างซ้าย
name2=("  sitthikon  ")
name2=name2.lstrip()
print(name2)
print(len(name2))
#ลบช่องว่างขวา
name2=("  sitthikon  ")
name2=name2.rstrip()
print(name2)
print(len(name2))

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)