def calculate(N,A,k):
    if(N==1):
        return [1],1
    l=1000000000
    B=[-1]
    for i in range(k-1,-1,-1):
        if(N>=A[0]):
            if(N%A[i]==0):
                count=0
                while(N%A[i]==0):
                    N//=A[i]
                    count+=1
                B,lb=calculate(N,A,k-1)
                if(lb<l):
                    x=B[-1]
                    l=lb
                    l+=count
                    for p in range(count):
                        x*=A[i]
                        B.append(x)

    return B,l
N,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
A.sort()
B,l=calculate(N,A,k)
print(*B)
