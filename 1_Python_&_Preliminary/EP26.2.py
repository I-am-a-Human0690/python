#ต่อ str concatinate
fname="sitthikon"
lname="chomphuphuen"
age="20"
salary=10000000000.0000
text="ชื่อ : {}\tนามสกุล : {}\tอายุ : {}"
print(text.format(fname,lname,age))
text2="ชื่อ : {1}\tนามสกุล : {0}\tอายุ : {2}\tเงินเดือน : {3:.2f}" #แล้วแต่เราจะเลือกให้อะไรอยู่ตรงไหน
print(text2.format(fname,lname,age,salary))