
n=int(input())
A=list(int(i) for i in input().split())
T=[0]*(n+1)
def update(ind,value):
    while(ind<=n):
        T[ind]+=value
        ind+=ind&(-ind)

def query(x):
    s=0
    while(x>0):
        s+=T[x]
        x-=x&(-x)
    return s 
for i in range(n):
    update(i+1,A[i])
Q=int(input())
for i in range(n):
    l=int(input())
    print(query(l))
