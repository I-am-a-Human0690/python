#Encapsulation
#protectes
#class
class Employee:
    def __init__(self,name,salary,department): 
        #protectes attribute
        self._name=name
        self._salary=salary
        self._department=department 
        self._showdata() #protectes สามารถเรียกจากทั้งข้างนอกแหละในได้

        #protectes methon
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self._salary))
        print("ตำแหร่ง = {}".format(self._department))

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1._name = "b"
print(obj1._name)
obj1._showdata()