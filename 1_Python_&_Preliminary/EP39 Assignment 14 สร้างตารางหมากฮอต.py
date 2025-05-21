#สร้างตารางหมากฮอต
'''
สีขาว = คู่ = x
สีดำ  = คี่ = o
0+0=x
0+1=o

1+0=o
1+1=o
'''
'''
a=int(input("กรอกตัวเลข : "))
for b in range(a):
     for c in range(a):
         if (b+c)%2 == 0:
            print("x",end="")
         else:
            print("o",end="")
     print("")
'''
a=int(input("กรอกตัวเลข : "))
for b in range(a):
     for c in range(a):
         print("x",end="")if(b+c)%2==0 else print("o",end="")
     print("")