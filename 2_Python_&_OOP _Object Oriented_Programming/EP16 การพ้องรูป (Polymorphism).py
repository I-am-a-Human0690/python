#การพ้องรูป
'''
การพ้องรูป (POLYMORPHISM)
Polymorphism เกิดจาก poly (หลากหลาย) + morphology (รูปแบบ)
                          Shape
                          draw()

Triangle                 Rectangle                 Circle
draw()                    draw()                   draw()
                         Polymorphism
ในทางโปรแกรมคือการที่เมธอดชื่อเดียวกัน สามารถรับอาร์กิวเมนต์ที่แตก
ต่างกันได้หลายรูปแบบ โดยเมรอดนี้จะถูกเรียกว่า overload method 
(เมรอดฤกโอเวอร์โหลด)

OVERLOADING & OVERRIDING METHOD
Over loading method คือ เมรอดที่มีชื่อเหมือนกันและอยู่ภายในคลาส
เดียวกัน สิ่งที่แยกความแตกต่างของเมรอดที่เป็น overload method
คือ พารามิเตอร์ (เป็นผลมาจากคุณสมบัติ 00 คือ polymorphism)

Overriding method คือ เมรอดของคลาสลูก (subclass) ที่มีชื่อเหมือน
กับเมธอดของคลาสแม่ (superclass) (เป็นผลมาจากคุณสมบัติ 00
คือ inheritance)
'''
