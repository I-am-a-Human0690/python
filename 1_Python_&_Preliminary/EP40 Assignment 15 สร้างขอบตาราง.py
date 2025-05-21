#สร้างขอบตาราง
'''
a=int(input("กรอกตัวเลข : "))
for b in range(a):
     for c in range(a):
         if b==0 or b==a-1 or c==0 or c==a-1:
            print("x",end="")
         else:
             print(" ",end="")
     print("")
'''
a=int(input("กรอกตัวเลข : "))
for b in range(a):
     for c in range(a):
         print("x",end="") if b==0 or b==a-1 or c==0 or c==a-1 else print(" ",end="")   
     print("")