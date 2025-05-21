#การแยกไฟล์เพื่อง่ายต่อการจัดการ
from EP18b import Accounting
from EP18c import Programmer
from EP18e import Sale

accounting =  Accounting("a",1000,30)
accounting._showdata()
print(accounting.__str__())
print(accounting._getincom())
print('')

programmer = Programmer("b",2000,"afghf","bgfgf")
programmer._showdata()
print(programmer.__str__())
print(programmer._getincom())
print('')

sale = Sale("c",3000,"a")
sale._showdata()
print(sale.__str__())
print(sale._getincom())