'''
Constructor
เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ
(ไม่ระบุก็ได้)
โครงสร้าง Constructor
def __init__(self):
nass

Destructor
เป็น Method พิเศษที่ตรงข้ามกับ Constructor จะถูกใช้งานเมื่อ
สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย 0bject ส่วนใหญ่
จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
โครงสร้าง Destructor
def del__(self):
nass
'''
#class
class Employee:
    def __init__(self,name,salary,department): #ถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ
        self.name=name
        self.salary=salary
        self.department=department 

    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหร่ง = {}".format(self.department))

    def __del__(self):
        print("Call Constuctor")#ถูกใช้งานเมื่อสิ้นสุดการทำงานของ class

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj2 = Employee("b",200000,"โปรแกรมเมอร์")
obj3 = Employee("b",300000,"โปรแกรมเมอร์")

#เรียกใช้
obj1.showdata()
obj2.showdata()
obj3.showdata()