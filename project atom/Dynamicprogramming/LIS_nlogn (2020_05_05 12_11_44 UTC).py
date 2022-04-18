INT_MAX=10**11+7
MOD=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
GETA=123
###############################################################################
import bisect as BS
n=int(input())
A=INPUT()
DP=[]
for i in range(n):
    if len(DP)==0:
        DP.append(A[i])
    else:
        if A[i]>DP[-1]:
            DP.append(A[i])
        else:
            ind=BS.bisect_left(DP,A[i],0,len(DP))
            DP[ind]=A[i]
print(len(DP))
