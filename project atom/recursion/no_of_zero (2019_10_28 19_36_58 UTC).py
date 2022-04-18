def zero(n,s):
    if(n==0):
        return 0
    r=n%10
    if(r==0):
        s+=1
    n=n//10
    s+=zero(n,0)
    return s
print(zero(2330040,0))
