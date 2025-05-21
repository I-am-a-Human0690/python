#kwargs มีข้อมูลเป็น ditionary
def a(**b):
    print(b,type(b))#<class 'dict'>
    print(b["q"],type(b["q"]))#ข้อมูลเป็น str

a(q="a",w="b",c=1)
print('')

#ไม่ได้
# a(a1=[1,3],a2=[1,2])

#ไม่ได้
# a1=2
# a2=2
# a(a1,a2)

#ไม่ได้
# a1=[1,2]
# a2=[1,2]
# a(a1,a2)



