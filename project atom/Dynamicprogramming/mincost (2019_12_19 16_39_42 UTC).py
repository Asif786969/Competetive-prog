for _ in range(int(input())):
    x=int(input())
    s=input()
    A=list(s)
    L=len(s)
    i=1
    bool=False
    while(i!=x):
        Lprev=L
        L=i+(L-i)*(int(A[i-1]))
        i+=1
        print(*A)
        if(bool is False):
            count=int(A[i-1])
            B=A[:i]
            C=A[i:]
            A=B+C*count
            if(L>10**6):
                bool=True
    print(L)
