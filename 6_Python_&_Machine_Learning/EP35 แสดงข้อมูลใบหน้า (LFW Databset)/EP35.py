'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-8-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%94%E0%B8%88%E0%B8%B3%E0%B9%83%E0%B8%9A%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-face-recognition-f7ec4629217c
สรุป Machine Learning(EP.8) — การจดจำใบหน้า (Face Recognition)
pip install -U scikit-learn
'''
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
#download & display image
faces=fetch_lfw_people(min_faces_per_person=60)#min_faces_per_person=60 ข้อมูลใบหน้าของแต่ละคน 60 แบบ
print(faces.target_names) #ชื่อเจ้าของใบหน้า
print(faces.images.shape)

print(faces.target)

fig,ax=plt.subplots(3,5)#กำหนด แถว คอลัม ที่จะแสดงรูป #fig=Figure(640x480) #ax=3แถว5คอลัม
print(ax)
print(fig)
'''
ตัววนซ้ำ 1 มิติบนอาร์เรย์ ระบุ index แบบ 1 มิติ
array([[1, 2, 3],
       [4, 5, 6]])
x.flat[3]
4
numpy.ndarray.flat
https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html
'''
for i,axi in enumerate(ax.flat):
    print(axi,i)#เก็บ fig,ax  i เก็บ index
    axi.imshow(faces.images[i],cmap='bone')
    #axi.set(xticks=[],yticks=[])#ถ้าไม่ระบุแบบนี้ ผลดูในรูป
    axi.set(xticks=[],yticks=[])
    axi.set_ylabel(faces.target_names[faces.target[i]].split()[-1],color="black")#setชื่อไว้แกน y แต่ละภาพ#.split()[-1] ดูในรูป
    
plt.show()
'''
https://www.devdit.com/post/1042/python-split-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%84%E0%B8%B3%E0%B8%AA%E0%B8%B1%E0%B9%88%E0%B8%87%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%97%E0%B8%B3%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3
Python Split คือคำสั่งอะไร ใช้ทำอะไร
Python Split คือ คำสั่งสำหรับแยกข้อความเป็นแต่ละรายการ ด้วยอักษร หรือข้อความที่ต้องการ เช่น แยกข้อความด้วยช่องว่าง 
หรือแยกข้อความด้วยขีดกลาง ผลลัพธ์คืนค่าเป็นตัวแปรชนิด List สามารถเขียนโปรแกรมได้ดังนี้

ตัวอย่างที่ 1 Python Split แยก String ด้วยช่องว่าง

txt = "Welcome to Devdit Thankyou :)"
s = txt.split(' ')
print( s )

ผลลัพธ์
['Welcome', 'to', 'Devdit', 'Thankyou', ':)']
 

ตัวอย่างที่ 2 Python Split แยก String ด้วยขีดกลาง (-)

txt = "Welcome-to-Devdit-Thankyou-:)"
s = txt.split('-')
print( s )

ผลลัพธ์
['Welcome', 'to', 'Devdit', 'Thankyou', ':)']
'''
