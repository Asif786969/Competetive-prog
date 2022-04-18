def INPUT():return list(int(i) for i in input().split())
n=5
A=[1,2,3,4,5]
T=[0]*(2*n)
for i in range(n):
    T[n+i]=A[i]
for i in range(n-1,0,-1):
    T[i]=T[2*i]+T[2*i+1]
def query(l,r):
    l-=1
    res=0
    #sum in given range
    l+=n
    r+=n
    while(l<r):
        if l&1:
            res+=T[l]
            l+=1
        if r&1:
            r-=1
            res+=T[r]

        l//=2
        r//=2
    print(res)
for i in range(1):
    l=1
    r=5
    query(l,r)
