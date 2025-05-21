'''
Setter , Getter Method
Setter การกำหนดค่าให้ Object
def setName(self,newname):
self.__name = newname
Gettter การดึงค่าจาก Object
def getName(self):
return self.__name
'''
#private
#class
class Employee:
    def __init__(self,name,salary,department): 
        #private attribute
        self.__name=name
        self.__salary=salary
        self.__department=department 

         #protectes methon
    def _showdata(self):
        print("ชื่อพนักงาน = "+(self.getName()))
        print("เงินเดือน = ",format(self.getName2()))
        print("ตำแหร่ง = "+(self.getName3()))

    #setter methon
    def setName(self,newname):
        self.__name = newname

    #Gettter methon
    def getName(self):
        return self.__name

    #Gettter methon
    def getName2(self):
        return self.__salary

    #Gettter methon
    def getName3(self):
        return self.__department

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1.setName("b")
print(obj1.getName())
obj1._showdata()
