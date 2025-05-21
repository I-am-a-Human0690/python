#superset
a={1,2,3,4,5,6}
#subset
b={1,2}
c={1,7}
print(b,c.issubset(a))
print(" ")

print(b.issubset(a)) #b เป็น subset a หรือไม่  ใช่
print(b.issuperset(a))#b เป็น superset a หรือไม่ ไม่
print(" ")

print(a.issuperset(b))#a เป็น superset b หรือไม่ ใช่
print(a.issubset(b))#a เป็น subset b หรือไม่  ไม่
print(" ")

print(c.issubset(a)) #c เป็น subset a หรือไม่  ใช่แค่ตัวเดียวเลยถือว่าไม่ใช่
print(c.issuperset(a))#c เป็น superset a หรือไม่ ไม่
print(" ")

print(a.issubset(c))#a เป็น subset c หรือไม่  ไม่
print(a.issuperset(c))#a เป็น superset c หรือไม่ ไม่ ใช่แค่ตัวเดียวเลยถือว่าไม่ใช่

