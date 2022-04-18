import sys
sys.setrecursionlimit(10000)
p=10**9+7
def fact(a):
    ans=1
    while(a!=0):
        ans*=a
        a-=1
    return ans
def calculate(x,m):
    if m==0 or x==m:
        return 1
    return calculate(x-1,m-1)+calculate(x-1,m)
n=100000
r=23
#print(calculate(n,r))

print((fact(n)//(fact(r)*fact(n-r)))%p)
