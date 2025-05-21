#ตัวดำเนินการทางตรรกศาสตร์
#and และ  ถ้ามีตัวใดตัวหนึ่ง เป็น false จะเป็น false
#or หรือ ถ้ามัตัวใดตัวหนึ่ง เป็น true จะเป็น true
#not ไม่ ใส่ข้างหน้าตัวที่จะทำให้ผลเป็นตรงข้าม print(not a)ต้องเว้นวรรคด้วย
a=(5>10)#ค่า a =bool
b=(1==1)#ค่า b =bool
c=a and b
d=a or b
print(c)
print(d)
print(not c)
print(not d)