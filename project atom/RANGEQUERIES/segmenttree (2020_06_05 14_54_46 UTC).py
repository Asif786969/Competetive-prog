def INPUT():return list(int(i) for i in input().split())
N,Q=INPUT()
A=INPUT()
T=[0]*2*N
for i in range(n):
    T[n+i]=A[i]
for i in range(n-1,0,-1):
    T[i]=T[2*i]+T[2*i+1]
def update():
    for i in range(n):
def query(l,r):
    res=0
    #sum in given range
    l+=n
    r+=n
    while(l<r):
        if l&1:
            res+=tree[l]
            l+=1
        if r&1:
            r-=1
            res+=tree[r]

        l//=2
        r//=2

for i in range(Q):
    l,r=INPUT()
    query(l,r)
