#สร้าง methon
'''
Attribute เป็นกลไกที่กำหนดคุณสมบัติให้กับคลาส
การสร้างAttribute
self.name ชื่อพนักงาน
self.salary เงินเดือน

Methon
การสร้าง Methon          การเรียกใช้
def getName(self):     ชื่อวัตถุ.getName()
    return self.name

คีย์เวิร์ด Self
การใช้คีย์เวิร์ด self จะเป็นตัวขี้หรือตัวที่บ่งบอกว่า
ตอนนี้เราทำงานกับวัตถุใด ให้บอกตัวตนของวัตถุนั้นๆ
เช่น การกำหนดคุณสมบัติต่างๆ ในวัตถุ เป็นต้น

'''
#class
class Employee:
      #สร้าง methon
    def detail(self):
        self.name="Sitthikon"
        self.salary= 10000000
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))


#การสร้างวัถุ
emp1 = Employee()
emp1.detail()