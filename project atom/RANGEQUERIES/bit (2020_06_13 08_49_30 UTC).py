#binary trees work only for cumulative sums
# if we want to update a range query in [l,r] and increment every thing by x
# we can do it by update(l,x)-update(r+1,-x)
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
for i in range(int(input())):
    x,y,z=list(input().split())
    y=int(y)
    z=int(z)
    if x=="c":
        print(query(z)-query(y-1))
    else:
        update(y,z-A[y-1])
        A[y-1]=z
