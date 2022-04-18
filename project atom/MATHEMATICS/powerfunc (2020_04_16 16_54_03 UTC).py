x=10**9+7

def power(a,n):
    if n==0:
        return 1
    else:
        if(n%2==0):
            return ((power(a,n//2))**2)%x
        else:
            return ((a%x)*(((power(a,(n-1)//2)))**2)%x)%x

ans=power(2,10**9)
print(ans)
