#Loop ซ้อน Loop
print("\twhile")
a=1
while a<=3:
    print("รอบที่ = ",a)
    b=1
    while b<=3:
        print("ตำแหน่งที่ = ",b)
        b+=1
    a+=1
print("\tFor")
for c in range(1,4):
    print("รอบที่ = ",c)
    for D in range(1,4):
        print("ตำแหน่ง = ",D)