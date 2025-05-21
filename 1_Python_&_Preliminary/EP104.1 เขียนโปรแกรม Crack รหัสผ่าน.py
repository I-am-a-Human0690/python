#random จนกว่าจะถูกรหัส
import random

ATM_PASSWORD="a1"
result=""

while result!=ATM_PASSWORD:
    result=""
    for letter in range(len(ATM_PASSWORD)):
        list_number=random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
        result="".join(list_number)+(result)
        print("SEARCH = ",result)
print("CEACK PASSWORD IS ",result)

