#Encapsulation
#public
#class
class Employee:
    def __init__(self,name,salary,department): 
        #public attribute
        self.name=name
        self.salary=salary
        self.department=department 
        self.showdata() #public สามารถเรียกจากทั้งข้างนอกแหละในได้

        #public methon
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหร่ง = {}".format(self.department))

#การสร้างวัถุ
obj1 = Employee("a",100000,"บัญชี")
obj1.name = "b"
print(obj1.name)
obj1.showdata()
