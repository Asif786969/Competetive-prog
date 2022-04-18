def subset(A,k):
    if(len(A)==0):
        if(k>0):
            b=[[0]]
            return b
        return None
    #excluding
    Bsubs=subset(A[1:],k)
    if(Bsubs!=None):
        new=[]
        for ele in Bsubs:
            new.append(ele)
        #including
        Asubs=subset(A[1:],k-A[0])
        if(Asubs!=None):
            for ele in Asubs:
                ele.append(A[0])
                for ele in Asubs:
                    new.append(ele)
            return new



#n=int(input())
#A=list(int(i) for i in input().split())
#k=int(input())
A=[1,20,5,1,4,2]
k=6
li=subset(A,k)
print(li)
