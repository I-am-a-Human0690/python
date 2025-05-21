#tower of hanoi
def hanoi(n,a,b,c):
    if(n==0):
        return
    hanoi(n-1,a,c,b)
    print(" จานที่ = ",n ," จาก = ",a," ไป = ",c)
hanoi(3,"A","B","C")

#def hanoi(3,a,b,c):
    #if(n==0):
        #return
    #hanoi(3-1,a,c,b)
            #=def hanoi(2,a(a),b(c),c(b)):
                #if(n==0):
                    #return
                #hanoi(2-1,a,c,b)
                    #=def hanoi(1,a(a),b(b),c(c)):
                        #if(n==0):
                            #return
                        #hanoi(0,a,c,b)
    #print(" จานที่ = ",1 ," จาก = ",a(a)," ไป = ",c(c)) = 1-a-c
    #print(" จานที่ = ",2 ," จาก = ",a(a)," ไป = ",c(b)) = 2-a-b
    #print(" จานที่ = ",3 ," จาก = ",a," ไป = ",c) = 3-a-c
#hanoi(3,"A","B","C")
#1-a-c
#2-a-b
#3-a-c
#หรือ
'''
#1 def hanoi(n,a,b,c):=3abc
    if(n==0):
        return
    hanoi(n-1,a,c,b) #2 3-1= 2 a c b=a(a) b(c) c(b)
    #1print(" จานที่ = ",n ," จาก = ",a," ไป = ",c)=3-a-c

#2 def hanoi(n,a,b,c):= 2 a c b=a(a) b(c) c(b)
    if(n==0):
        return
    hanoi(n-1,a,c,b) #3 = 2-1=1(a) b(c) c(b) = a(a) b(b) c(c)
    print(" จานที่ = ",n ," จาก = ",a(a)," ไป = ",c(b))=2-a-b

#3    def hanoi(n,a,b,c):=1 a(a) b(b) c(c)
    if(n==0):
        return
    hanoi(1-1,a,c,b)
    #3print(" จานที่ = ",n ," จาก = ",a(a)," ไป = ",c(c))=1-a-c
hanoi(3,"A","B","C")

hanoi(3,"A","B","C")
#3=1-a-c
#22-a-b
#1=2-a-b
'''
