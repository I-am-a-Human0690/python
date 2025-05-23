'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-4-%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%88%E0%B8%B3%E0%B9%81%E0%B8%99%E0%B8%81%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B9%84%E0%B8%9A%E0%B8%A3%E0%B8%B2%E0%B8%A3%E0%B8%B5%E0%B9%88-binary-classifier-6ebc8e1a5e61
'''
'''
สรุป Machine Learning(EP.4)- ตัวจำแนกแบบไบรารี่ (Binary Classifier)

เส้น Hyperplane แบ่งข้อมูลออกเป็น 2 ส่วน
ตัวจำแนกแบบไบนารี (Binary Classifier) เป็นวิธีการแบ่งข้อมูลออกเป็น 2 กลุ่ม (Binary Class) 
จากภาพตัวอย่างจะแบ่งข้อมูลออกเป็น 2 กลุ่ม คือ กลุ่มสีแดงและกลุ่มสีน้ำเงิน (Class สีแดง และ Class สีน้ำเงิน)โดยใช้เส้น Hyperplane
(เส้นสมมุติ | เส้น Linear Regression) แบ่งกลุ่มข้อมูลทั้ง 2 กลุ่มแยกออกจากกัน


Target MNIST Dataset
ภายใน LAB จะยกตัวอย่างเพื่อให้เห็นการแบ่งกลุ่มของข้อมูลโดยใช้ MNIST Dataset ว่าข้อมูลกลุ่มใดแสดงกลุ่มตัวเลข 0–9 
โดยข้อมูลทั้งหมดจะมี 70,000 ชุดจะต้องเขียนโปรแกรมแบ่งข้อมูลออกเป็น 2 ส่วนได้แก่
- Training Set 60,000 ชุด
- Test Set 10,000 ชุด

จากบทที่ 1 :การแบ่งชุดข้อมูล MNIST Dataset

ข้อมูลชุดเรียนรู้ (Training Set) จัดเรียงและแบ่งกลุ่มเป็น Class 0 — Class 9
ข้อมูลชุดทดสอบ (Test Set) จัดเรียงและแบ่งกลุ่มเป็น Class 0 — Class 9
Gradient Descent Algorithm (GD)— อัลกอริทึมสำหรับใช้หาจุดต่ำสุดหรือสูงสุดของฟังก์ชั่นที่กำหนดขึ้นมาโดย
ใช้วิธีการวนหาค่าที่ทำให้ได้ค่าต่ำสุดจากการคำนวณความชัน ณ จุดที่เราอยู่แล้วพยายามเดินไปทางตรงข้ามกับกับความชันนั้
'''