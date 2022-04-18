def minmoves(A,x):
    p=0
    valuable=[]
    for ele in A:
        if(x-ele[0]+ele[1]>=x):
            p+=1
            valuable.append(-1)
        else:
            valuable.append(1)
    if(p==3):
        return -1
    dp=[]
    while




T=int(input())
for i in range(T):
    n,x=list(int(i) for i in input().split(" "))
    A=[]
    for i in range(n):
        d,h=list(int(i) for i in input().split(" "))
        A.append([d,h])
    print(minmoves(A,x))
