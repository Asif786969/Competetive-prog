INT_MAX=10**18+7
MOD=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#################################################################################
from random import randint
Factorial=[1 for i in range(10**6+1)]
for i in range(1,10**6+1):
    Factorial[i]=(Factorial[i-1]*i)%MOD
def power(a,n):
    res=1
    while(n>0):
        if n&1:
            res=(res*a)%MOD
        a=(a*a)%MOD
        n//=2
    return res
for _ in range(10**5):
    n=randint(10000,999999)
    x=n-1
    ans=((2*n)%MOD *Factorial[x] * power(Factorial[x//2],MOD-2) * power(Factorial[x-x//2],MOD-2) * power(2**n,MOD-2))
    print(ans%MOD)
