# Module Date / Time
import datetime
from time import strftime 
a=datetime.datetime.now() #ดึงเวลาปัจจุบันมาใช้
print(a) #แสดงทั้งหมด
print(a.year) #แสดงปี
print(a.month) #แสดงเดือน
print(a.day) #แสดงวัน
#และอื่นๆ
print('')

#กำหนดเอง
b=datetime.datetime(2022,4,12,15,12,12,12) #y/m/d/h/m/n/เล็กกว่าวินาที
print(b)
print('')
#รูปแบบการแสดงผล
print("เริ่มต้น",a)
#แสดงแบบสั้น
print(a,strftime("%x")) #m/d/y      04/13/22
print(a,strftime("%X")) #เวลา        15:36:08
print(a,strftime("%c")) #d/m/d/h    Wed Apr 13 15:36:08 2022
print('')

#เวลา
print(a.strftime("%H:%M:%S %p")) #15:36:08 PM
print('')

#ลำดับในปี 1-366
print(a,strftime("%j")) #103
print('')

#date
print(a,strftime("%a")) # แบบสั้น    Wed
print(a,strftime("%A")) # แบบเต็ม    Wednesday
print(a,strftime("%w")) # ลำกับในวัน  sunday = 0
print(a,strftime("%d")) # วันที่
print(a,strftime("%b")) # เดือนแบบสั้น
print(a,strftime("%B")) # เดือนแบบยาว
print('')

print(a,strftime("%A%d%B%Y")) #แบบติดกัน
print(a,strftime("%A %d %B %Y")) #แบบดว้นวรรค
print(a,strftime("a %A b %d")) #ใช้ภาษาไทยไม่ได้
print('')

# ว/ด/ป
print(a,strftime("%d %m %B %Y"))