
#Inheritance
#การสืบทอดคุณสมบัติ  แปลง Object เป็น String
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
    
    #รายได้ต่อปี
    def _getincom(self):
        return self.__salary*12
    
    def __str__(self):
        return ("ชื่อพนักงาน = {} เงินเดือน = {} ตำแหร่ง = {}".format(self._name,self.__salary,self.__department))

class Accounting(Employee):
    _departmentname = "แผนกบัญชี"
    def __init__(self,name,salary): #ส่งลงข้างล่าง
        super().__init__(name,salary,self._departmentname)#ส่งเข้า constructor คลาสแม่

class Programmer(Employee):
    def __init__(self,name,salary,department): 
        super().__init__(name,salary,department)

class Sale(Employee):
    _departmentname = "ฝ่ายขาย"
    def __init__(self,name,salary): 
        super().__init__(name,salary,self._departmentname)
        super()._showdata()

accounting =  Accounting("a",1000)
print("รายได้ต่อปี = {} ".format(accounting._getincom( )))
print(accounting.__str__())
print('')
programmer = Programmer("b",2000,"โปรแกรมเมอร์")
print("รายได้ต่อปี = {} ".format(programmer._getincom( )))
print(programmer.__str__())
print('')
sale = Sale("c",3000)
print("รายได้ต่อปี = {} ".format(sale._getincom( )))
print(sale.__str__())