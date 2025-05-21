#for
a=dict({"red":"สีแดง","blue":"สีฟ้า"})
for b in a:
    print(b)
print('1')
for b in a:
    print(a[b])
print('2')

for b in a.values():
    print(b)
print('3')

for b in a.keys():
    print(b)
print('4')

for b in a.items():
    print(b)
print('5')

for b,c in a.items():
    print(b,c)
print('6')

for b,c in a.items():
    print(b)
print('7')

for b,c in a.items():
    print(c)
print('8')

