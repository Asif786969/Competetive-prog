#works only for sorted arrays
n=10
A=[1,2,3,4,5,6,8,67,90,96]
x=96
def binsrch(A,x,n):
    s=0
    e=n-1
    while(s<e):
        mid=(s+e)//2
        if(A[mid]>x):
            e=mid-1
        elif(A[mid]<x):
            s=mid+1
        elif(A[mid]==x):
            return mid+1
    if(s==e):
        if(A[s]==x or s==0):
            return s+1
        if(s!=0):
            return s+2
    if(s!=e):
        return s+1



print(binsrch(A,x,n))
