def INPUT():return list(int(i) for i in input().split())
n=5
A=[1,2,3,4,5]
T=[0]*(2*n)
for i in range(n):
    T[n+i]=A[i]
for i in range(n-1,0,-1):
    T[i]=T[2*i]+T[2*i+1]
def update(ind,val):
    ind+=n
    T[ind]=val
    ind//=2
    while(ind>0):
        T[ind]=T[2*ind]+T[2*ind+1]
        ind//=2


def query(l,r):
    res=0
    l+=n
    r+=n
    while(l<=r):
        if l&1:
            res+=T[l]
            l+=1
        if r&1:
            res+=T[r]
            r-=1
        l>>=1
        r>>=1
    print(res)
print(T)
for i in range(1):
    l=1
    r=1
    query(l,r)
