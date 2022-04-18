INT_MAX=10**18+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#################################################################################
import math
d,s,n=INPUT()
def calc(l,k,m):
    if s*l+d-s>=k:
        return -1
    alpha=l**2 +l +2*k*m
    D=math.sqrt(9+4*alpha)
    Q=int(D)
    if Q%2==0:
        Q=Q-1
        r=(Q-3)//2
        if r>=l:
            if r**2 + 3*r - alpha<=0:
                #nothing to do
            else:
                Q+=2

    else:
        r=(Q-3)//2
        if (r+1)**2 + 3*(r+1) -alpha<=0 and (r+1)>=l:
            Q+=2
        elif (r)**2 +3*r -alpha<=0 and r>=l:
            #nothing
        else:
            Q-=2
    ans=(Q-3)//2
    return ans

for _ in range(n):
    l,k,m=INPUT()
    print(calc(l,k,m))
