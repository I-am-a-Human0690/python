#class
class Employee:
      #สร้าง methon
    def detail(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหร่ง = {}".format(self.department))


#การสร้างวัถุ
obj1 = Employee()
obj1.detail("a",100000,"บัญชี")

obj2 = Employee()
obj2.detail("b",200000,"โปรแกรมเมอร์")

obj3 = Employee()
obj3.detail("b",300000,"โปรแกรมเมอร์")

#เรียกใช้
obj1.showdata()
obj2.showdata()
obj3.showdata()