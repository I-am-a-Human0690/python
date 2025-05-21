#Encapsulation
#private
#class
class Employee:
    def __init__(self,name,salary,department): 
        #private attribute
        self.__name=name
        self.__salary=salary
        self.__department=department 
        self.__showdata() #private ไม่สามารถเรียกจากข้างนอกได้ แต่เรียกจากข้างในได้

        #private methon
    def __showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหร่ง = {}".format(self.__department))

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1.__name = "b"
print(obj1.__name)
print(isinstance(obj1.__name,Employee))
# obj1.__showdata() ไม่สามามาถเรียกใช้งานได้