from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
########################################################
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
