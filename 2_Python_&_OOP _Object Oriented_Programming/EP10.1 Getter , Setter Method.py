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
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหร่ง = {}".format(self.__department))

    #setter methon
    def setName(self,newname):
        self.__name = newname

    #Gettter methon
    def getName(self):
        return self.__name
        


#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1.setName("b")  #ถ้าเป็น#private  __showdata(self):
print(obj1.getName())
obj1._showdata()

