'''
คีย์เวิร์ด super
เมื่อต้องการเรียกใช้งานคุณบัติต่างๆในคลาสแม่ เช่น
Constructor , Method , Attribute
super().__init__(name)
'''
#Inheritance
#การสืบทอดคุณสมบัติ
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

class Accounting(Employee):
    _departmentname = "แผนกบัญชี"
    def __init__(self): 
        pass
class Programmer(Employee):
    _departmentname = "โปรแกรมเมอร์"
    def __init__(self): 
        pass
class Sale(Employee):
    _departmentname = "ฝ่ายขาย"
    def __init__(self): 
        pass

accounting =  Accounting()
print(accounting.a1)
print(accounting._a2)
print(accounting._Employee__a3) #print(accounting.__a3) ไม่ได้
print(accounting._departmentname)

programmer = Programmer()
print(programmer._departmentname)

sale = Sale()
print(sale._departmentname)