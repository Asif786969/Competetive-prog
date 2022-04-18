q=int(input())
for i in range(q):
    m,r=list(int(i) for i in input().split())
    A=list(int(i) for i in input().split())
    A.sort()
    prev=-1
    B=[]
    for i in range(m):
        if(A[i]!=prev):
            B.append(A[i])
            prev=A[i]
    l=len(B)
    if(l==1):
        print(1)
    else:
        bomb=0
        while(l>0 and B[-1]>0):
            #dropping at right most
            bomb+=1
            B.pop()
            l-=1
            if(l>0):
                B[-1]-=r*bomb
        print(bomb)
