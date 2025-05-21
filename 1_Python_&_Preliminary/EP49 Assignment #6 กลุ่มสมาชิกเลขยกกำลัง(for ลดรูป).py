#หาค่ายกกำลัง
a=[1,2,3,4,5,6,7]
print(a)
#เขียนแบบปกติ
for b in range(len(a)):
    a[b]=a[b]**2
print(a)
#ลดรูป
d=[1,2,3,4,5,6,7]
print([c*c for c in d])
# print('d') for c in d  ไม่ได้
z = [c*c for c in d]
print(z)
    

