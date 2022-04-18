def calculate(N,A,k):
    if(N==1):
        return [1],1
    l=1000000000
    B=[-1]
    for i in range(k):
        if(N%A[i]==0):
            B,lb=calculate(N//A[i],A,k)
            if(lb<l):
                B.append(N)
                l=lb+1
    return B,l
N,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
A.sort()
B,l=calculate(N,A,k)
print(*B)
