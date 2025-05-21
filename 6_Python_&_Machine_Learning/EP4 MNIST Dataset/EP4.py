'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-2-%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B8%97%E0%B8%94%E0%B8%AA%E0%B8%AD%E0%B8%9A-119a16a901c8
'''
'''
กระบวนการ Machine Learning จะแบ่งข้อมูลสำคัญๆออกเป็น 2 ส่วน คือ

ข้อมูลชุดเรียนรู้ (Training Set) ถูกนำไปเรียนรู้ด้วยวิธีการเรียนรู้เครื่องจักรเพื่อสร้างเป็นโมเดล (Model) จะประกอบไปด้วย label / class เพื่อบอกว่าข้อมูลชุดนี้คืออะไร เช่น ชุดข้อมูลตัวเลข 0–9 , ข้อมูลสายพันธ์สุนัข เป็นต้น
ข้อมูลชุดทดสอบ (Test Set) ใช้ทดสอบโมเดลที่สร้างขึ้น หากโมเดลที่ทดสอบมีประสิทธิภาพดีจึงจะนำไปใช้งานจริง
'''

from sklearn  import datasets
digit_datasct=datasets.load_digits()
print('keys')
print(digit_datasct.keys())
print('target')
print(digit_datasct['target'])
print(digit_datasct.target)#แบบนี้ก็ได้
print('target_names')
print(digit_datasct['target_names'])
print('DESCR')
print(digit_datasct['DESCR'])
print('feature_names')
print(digit_datasct['feature_names'])
print('data')
print(digit_datasct['data'])
print('data[0:10]')
print(digit_datasct['data'][0:2])
print('images')
print(digit_datasct['images'].shape)#ขนาด 8*8 pix
print(digit_datasct.images[0])
print(digit_datasct.images[0].shape)#เช็คว่าเลขอะไร