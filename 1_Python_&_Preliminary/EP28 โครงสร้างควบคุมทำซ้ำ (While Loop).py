#โครงควบคุมแบบทำซ้ำ
#จะทำจนกว่าจะไม่เป็นจริง
#while
a=1
z=3
while a<=3:
    print("รอบที่ ",a)
    a+=1
print("จบโปรแกรม")
#for
for a in range(1,5):
    print(a)
print(" ")
for b in range(1,10,2):
    print(b)
print(" ")
d=[1,2,z,4,"a"]
for c in d:
    print(c)

# num_list = [ 1,2,3,4 ]
# result = 0
# for i in num_list :
#     if i == 5 :
#         break
#     print ( i )
#     result += i
# else :
#     print ( ' Sum : ' , result )
print("----------------------------")
num_list = [ 1,2,3,4]#[ 1,2,3,4,5]
result = 0
for i in num_list :
    if i == 5 :
        break
    print ( i )
    result += i
else :
    print ( ' Sum : ' , result )