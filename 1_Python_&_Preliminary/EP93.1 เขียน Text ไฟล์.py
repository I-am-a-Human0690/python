fw=open('Python/1_Python_&_Preliminary/EP93.1.txt',"w",encoding="utf-8")# W เป็นการสร้างไฟล์เพื่อเขียน  และถ้ามีอยู่แล้วจะเขียนทับอันเก่า
#ทดสอบความยาว
fw.writelines("jmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeoriwwwww442dfnsnryjmdmxyfmxjmf cfhxnfs/bknabknflkanwhpnbtinblgoianrwjbhnwrnbo idnbjrnwoihborajbno;biernobinaeosgihnboahrbnga;oebnaeori")
fw.writelines("qqqqq")
fw.writelines("1")
fw.writelines("\n555")
fw.close

fw=open('Python/1_Python_&_Preliminary/EP93.1.txt',"r")
print(fw.read())
fw.close

# fw=open("EP93.2.txt","r")
# print(fw.read())
# fw.close