#set operator คัวดำเนินการ
#union A=B.union(C) คือการรวมกันและ  หากตัวไหนซ้ำกันจะเก็บตัวเดียว
#difference A=B.difference(C) คือถ้า B มีตัวไหนซ้ำกับ C จะนำตัวนั้นออกจาก B
#difference_update A.difference_update(B)
#intersection A=B.intersection(C) คือการเก็บเฉพาะตัวที่ซ้ำกัน 
#intersection_update A.intersection_update(B)

#difference A=B.difference(C) -
a1={1,2,3}
a2={2,3,4,5}
print(a1-a2) #แบบนี้ก็ได้
#a1.difference(a2)จะไม่เกิดผล
a3=a1.difference(a2)
print(a3)
#difference_update A.difference_update(B)
a1.difference_update(a2)
print(a1)