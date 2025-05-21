class Employee:
    a1=100 
    _a2=200 
    __a3="asdas" 
    def __init__(self,name,salary,department): 
        self._name=name
        self.__salary=salary
        self.__department=department 

    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหร่ง = {}".format(self.__department))
    
    #รายได้ต่อปี
    def _getincom(self,bonus=0,overtime=0):
        return (self.__salary*12)+bonus+overtime
    
    def __str__(self):
        return ("ชื่อพนักงาน = {} เงินเดือน = {} ตำแหร่ง = {}".format(self._name,self.__salary,self.__department))