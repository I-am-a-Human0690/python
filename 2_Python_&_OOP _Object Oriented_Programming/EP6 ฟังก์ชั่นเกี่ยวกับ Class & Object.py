'''
isinstance และ dir คือฟังก็ชั่นที่ทำงานกับ claรs และ
object โดยมีรายละเอียดดังนี้
isinstance => เช็คว่า object นี้ถูกสร้างจาก clลรs ที่เรานิยามหรือไม่
dir => แสดง Attribute และ Method
__class__ => แสดงชื่อ class ของ object
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

    # def __del__(self):
    #     print("Call Constuctor")#ถูกใช้งานเมื่อสิ้นสุดการทำงานของ class

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj2 = Employee("b",200000,"โปรแกรมเมอร์")
obj3 = Employee("b",300000,"โปรแกรมเมอร์")

# #เรียกใช้
# obj1.showdata()
# obj2.showdata()
# obj3.showdata()

print(isinstance(obj1,Employee))#isinstance => เช็คว่า object นี้ถูกสร้างจาก clลรs ที่เรานิยามหรือไม่
print('')
print(dir(obj1))#dir => แสดง Attribute และ Method 
print('')
print(dir(obj1.name)) 
print('')
print(obj1.__class__)#__class__ => แสดงชื่อ class ของ object