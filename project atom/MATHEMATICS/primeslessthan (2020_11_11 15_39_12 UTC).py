#import math as M
def calc(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p**2<=n):
        if prime[p]==True:
            for i in range(p**2,n+1,p):
                prime[i]=False
        p+=1
    ans=[]
    for p in range(2,n):
        if prime[p]:
            ans.append(p)
    return ans
L=calc(10**6)
print(len(L))
