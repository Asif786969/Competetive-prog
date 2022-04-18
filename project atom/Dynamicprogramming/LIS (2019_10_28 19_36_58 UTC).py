#by recursion
def LIS(A):
    if(len(A)==1):
        return 1
    #excluding
    exc=LIS(A[1:])
    #including
    p=A[0]
    l=-1000000000
    for i in range(1,len(A)):
        if(A[i]>p):
            l=max(LIS(A[i:]),l)
    ans=max(l,exc)
    return ans


#n=int(input())
n=7
A=[1,2,3,4,0,78]
print(LIS(A))
