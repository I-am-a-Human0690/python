from EP18a import Employee
class Programmer(Employee):
    __departmentname = "โปรแกรมเมอร์"
    def __init__(self,name,salary,experience,skill): 
        super().__init__(name,salary,self.__departmentname)
        self.__exp=experience
        self.__skill=skill
    
    def _showdata(self):
        super()._showdata()
        print("ประสบการณ์ = "+self.__exp)
        print("ทักษะ = "+self.__exp)
    
    def __str__(self):
        return (super().__str__()+" ประสบการณ์ = {}  ทักษะ {}".format(self.__exp,self.__skill))