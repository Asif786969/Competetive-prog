#FOR HEAP THE PARENT VALUE IS GREATER THAN THE CHILD
#FOR MAXHEAP YOU CAN ONLY INCREASE THE VALUE OF A node
#IF YOU WANT TO DECREASE THE VALUE YOU HAVE TO BUILD MIN HEAP
#IT IS BASICALLY USED TO FIND THE MAX IN O1
#BINARY HEAP/PRIORITY QUEUE
INT_MAX=10**11+7
MOD=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#=======================================================================
n,q=list(int(i)for i in input().split())
A=list(int(i)for i in input().split())
T=[0]*(2*n)
for i in range(n):
    T[i+n]=A[i]
for i in range(n-1,0,-1):
    T[i]=min(T[i<<1],T[i<<1|1])
def query(l,r):
    res=10**19
    l+=n
    r+=n
    while(l<r):
        if l&1:
            res=min(T[l],res)
            l+=1
        if r&1:
            r-=1
            res=min(T[r],res)
        l//=2
        r//=2
    return res
def update(i,val):
    T[i+n]=val
    i+=n
    p=i
    while(p>1):
        T[p>>1]=min(T[p],T[p^1])
        p>>=1

for _ in range(q):
    c,l,r=list(input().split())
    l=int(l)
    r=int(r)
    if c=="q":
        print(query(l-1,r))

    else:
        update(l-1,r)
