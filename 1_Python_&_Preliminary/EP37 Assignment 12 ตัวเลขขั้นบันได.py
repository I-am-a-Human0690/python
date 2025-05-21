#ตัวเลขขั้นบันได
'''
number=int(input("ป้อน : "))
for row in range(1,number+1):
    for a in range(1,row+1):
        print(a,end='')
        print("..")
    print("")
'''
number=int(input("ป้อน : "))
for row in range(1,number+1):
    for a in range(1,row+1):
        print(a,end='')
    print("")