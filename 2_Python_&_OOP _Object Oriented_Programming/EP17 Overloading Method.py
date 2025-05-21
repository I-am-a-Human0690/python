#overloadding
'''
OVERLOADING & OVERRIDING METHOD
Overloading method คือ เมอดที่มีชื่อเหมือนกันและอยู่ภายในคลาส
เดียวกัน สิ่งที่แยกความแตกต่างของเมรอดที่เป็น overload method
คือ พารามิเตอร์ (เป็นผลมาจากคุณสมบัติ 00 คือ polymorphism)

Overriding method คือ เมรอดของคลาสลูก (subclass) ที่มีชื่อเหมือน
กับเมธอดของคลาสแม่ (superclass) (เป็นผลมาจากคุณสมบัติ 00
คือ inheritance)
'''
class Employee:
    a1=100 
    _a2=200 
    __a3="asdas" 
    def __init__(self,name,salary,department): 
        self._name=name
        self.__salary=salary
        self.__department=department 

    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหร่ง = {}".format(self.__department))
    
    #รายได้ต่อปี
    def _getincom(self,bonus=0,overtime=0):
        return (self.__salary*12)+bonus+overtime
    
    def __str__(self):
        return ("ชื่อพนักงาน = {} เงินเดือน = {} ตำแหร่ง = {}".format(self._name,self.__salary,self.__department))

class Accounting(Employee):
    _departmentname = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self._departmentname)
        self.__age=age

    def _showdata(self):
        super()._showdata()
        print("อายุ = "+str(self.__age))

    def __str__(self):
        return (super().__str__()+" อายุ = {}".format(self.__age))

class Programmer(Employee):
    __departmentname = "โปรแกรมเมอร์"
    def __init__(self,name,salary,experience,skill): 
        super().__init__(name,salary,self.__departmentname)
        self.__exp=experience
        self.__skill=skill
    
    def _showdata(self):
        super()._showdata()
        print("ประสบการณ์ = "+self.__exp)
        print("ทักษะ = "+self.__exp)
    
    def __str__(self):
        return (super().__str__()+" ประสบการณ์ = {}  ทักษะ {}".format(self.__exp,self.__skill))


class Sale(Employee):
    _departmentname = "ฝ่ายขาย"
    def __init__(self,name,salary,area): 
        super().__init__(name,salary,self._departmentname)
        self.__area = area

    def _showdata(self):
        super()._showdata()
        print("พื้นที่รับผิดชอบ = "+self.__area)
    
    def __str__(self):
        return (super().__str__()+" พื้นที่รับผิดชอบ = {}".format(self.__area))

accounting =  Accounting("a",1000,30)
accounting._showdata()
print(accounting.__str__())
print(accounting._getincom())
print('')

programmer = Programmer("b",2000,"afghf","bgfgf")
programmer._showdata()
print(programmer.__str__())
print(programmer._getincom())
print('')

sale = Sale("c",3000,"a")
sale._showdata()
print(sale.__str__())
print(sale._getincom())