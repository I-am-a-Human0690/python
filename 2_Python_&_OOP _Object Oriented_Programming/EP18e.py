from EP18a import Employee
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
        