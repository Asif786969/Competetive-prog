for _ in range(int(input())):
    x=int(input())
    A=list(input())
    L=len(A)
    i=0
    bool=False
    while(i!=x):
        i+=1
        count=int(A[i-1])
        L=i+(L-i)*(count)
        if(count>1):
            if(bool is False):
                C=A[i:]
                A=A+C*(count-1)
                if(L>10**6):
                    bool=True

    print(L%(10**9+7))
