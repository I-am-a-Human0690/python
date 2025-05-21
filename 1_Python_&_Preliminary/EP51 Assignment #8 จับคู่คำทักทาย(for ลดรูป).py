#จับคู่คำทักทาย / บุคคล
a=["้hi","hello","สวัสดี","Goodbye"]
b=["้ปอน","กร","พร"]
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print(c)
#ลดรูป
d=[z+s for z in a for s in b]
print(d)