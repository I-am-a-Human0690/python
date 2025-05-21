from EP18a import Employee
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