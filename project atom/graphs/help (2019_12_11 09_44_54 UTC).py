def gcd(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
def govr(r,b,k):
    GCD=gcd(r,b)
    LCM=(r*b)//GCD
    if(k>=LCM):
        return True
    else:
        blocksize=LCM//GCD-1
        if(blocksize<=k):
            return False
        else:
            return True


for _ in range(1):
    r=1
    b=1000000000
    k=999999998
    if govr(r,b,k) is True:
        print("OBEY")
    else:
        print("REBEL")
