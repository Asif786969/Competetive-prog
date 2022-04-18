from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
###############################################################################\
from sys import setrecursionlimit
setrecursionlimit(1000002)
import random as R
def calc(n,m,A):
    if n==0 or n<=A[0]:
        return 0
    ans=-1
    for i in range(m-1,-1,-1):
        if n%A[i]==0 and n!=A[i]:
            ans=max(1+(n//A[i])*calc(A[i],m,A),ans)
    return ans

def factors(n):
    P=[1]
    if n==1:
        return P
    i=2
    while(i<=math.sqrt(n)+1):
        if n%i==0:
            if n//i==i:
                P.append(i)
            else:
                P.append(i)
                P.append(n//i)
        i+=1
    P.append(n)
    return P
def calc2(A,F,n,m):
    dp=[[0 for i in range(len(F))]for j in range(m)]

    for i in range(m):
        for j in range(len(F)):
            if i==0:
                if F[j]%A[i]==0:
                    dp[i][j]=1
            else:
                if F[j]%A[i]==0 and F[j]>A[i]:
                    dp[i][j]=max(1,1+(dp[i][F.index(A[i])]*F[j])//A[i])
                else:
                    dp[i][j]=dp[i-1][j]
    # for ele in dp:
    #     print(ele)
    ans=0
    for ele in dp:
        ans=max(ans,max(ele))
    return ans

for  _ in range(1000):
    n=R.randint(1,100)
	m=R.randint(1,10)
	A=[]
	for i in range(m):
		A.append(R.randint(1,20))

    F=factors(n)
    F=list(set(F))
    F.sort()
    print(F)
    A=list(set(A))
    A.sort()
    x=calc(n,len(A),A)
    y=calc2(A,F,n,len(A))
	if x!=y:
		print(n,m,A)
		print(x,y)
		break
