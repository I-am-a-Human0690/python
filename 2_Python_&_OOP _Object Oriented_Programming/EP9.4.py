#Encapsulation
#ผสม
#class
class Employee:
    def __init__(self,name,salary,department): 
        #attribute
        self.name=name#public
        self._salary=salary#protectes
        self.__department=department #private
        self._showdata() 

        ##protectes methon
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))#public
        print("เงินเดือน = {}".format(self._salary))#protectes
        print("ตำแหร่ง = {}".format(self.__department))#private

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1.name = "b"#public แก้ไขได้
print(obj1.name)
print('')
obj1._salary = 10030#protectes แก้ไขได้
print(obj1._salary)
print('')
obj1.__department = "dfbdf" #private แก้ไขไม่ได้
print(obj1.__department)
print(isinstance(obj1.__department,Employee))
print('')
obj1._showdata() 