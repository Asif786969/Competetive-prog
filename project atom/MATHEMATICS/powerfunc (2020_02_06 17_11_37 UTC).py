x=10**9+7
#n,m=1,3
n,m=list(int(i) for i in input().split())
def power(a,n):
    if n==0:
        return 1
    else:
        if(n%2==0):
            return ((power(a,n//2))**2)%x
        else:
            return ((a%x)*(((power(a,(n-1)//2)))**2)%x)%x
first=power(2,m)
#print(first)
ans=power(first-1,n)
print(ans)
#THIS ONE HAS MINIMUM TIME COMPLEXITY O(log(n))
#SIMILARILY WE CAN CALCULATE x**n mod m by using mod m in every step
#MAKE SURE YOU USE (a.b)mod m=((a mod m)*(b mod m))*m
