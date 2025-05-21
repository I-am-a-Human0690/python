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
    pass
'''
#class
class Employee:
    def __init__(self):
        print("Default Constuctor") #ถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ
      #สร้าง methon
    def detail(self,name,salary,department):
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
obj1 = Employee()

obj2 = Employee()

obj3 = Employee()

# #การสร้างวัถุ
# obj1 = Employee()
# obj1.detail("a",100000,"บัญชี")

# obj2 = Employee()
# obj2.detail("b",200000,"โปรแกรมเมอร์")

# obj3 = Employee()
# obj3.detail("b",300000,"โปรแกรมเมอร์")

# #เรียกใช้
# obj1.showdata()
# obj2.showdata()
# obj3.showdata()