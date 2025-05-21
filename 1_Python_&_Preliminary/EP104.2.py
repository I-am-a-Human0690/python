#รหัสเป็น int
import random

ATM_PASSWORD=15
result=""

while result!=ATM_PASSWORD:
    result=""
    for letter in range(len(str(ATM_PASSWORD))):
        list_number=random.choice("0123456789")
        result="".join(list_number)+(result)
        print("SEARCH = ",result)
    result=int(result)
print("CEACK PASSWORD IS ",result)