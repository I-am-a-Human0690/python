'''
Class Variable & Instance Variable
Class Variable คือ ตัวแปรที่ทำงานภายใน class ส่วนอื่น
สามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attrbiute) โดยไม่
จำเป็นต้องสร้าง Object ขึ้นมา
Instance Variable คือ ตัวแปรที่อยู่ภายใน object สามารถ
เข้าถึงข้อมูลส่วนนี้โดยการต้องสร้าง Object ขึ้นมา
'''
class Employee:
    #class variable
    a1=100 #public
    _a2=200 #protectes
    __a3="asdas" #private
    def __init__(self,name,salary,department): 
        #Instance Variable
        self._name=name
        self.__salary=salary
        self.__department=department 

         #protectes methon
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหร่ง = {}".format(self.__department))

print(Employee.a1,type(Employee.a1)) #class variable
print(Employee._a2) #class variable
# print(Employee.__a3) #class variable
obj1 = Employee("a",100000,"บัญชี")
print(obj1._name) #Instance Variable
