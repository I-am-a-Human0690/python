fa=open('./Python/1Python_&_Preliminary/EP93.2.txt',"a",encoding="utf-8")
fa.writelines("")
for a in range(3):
    c=input(":")
    fa.writelines(c+"\n")
fa.close
fa=open('./Python/1Python_&_Preliminary/EP93.2.txt',"r",encoding="utf-8")
print(fa.read())
fa.close