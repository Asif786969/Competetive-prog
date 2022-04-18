def gcd(x, y):
    if x==y:
        return x
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
    r//=GCD
    b//=GCD
    if(r>b):
        r,b=b,r
    if((k - 1) * r + 1 < b):
		return False
	else
		return True


for _ in range(int(input())):
    r,b,k=list(int(i) for i in input().split())
    if govr(r,b,k) is True:
        print("OBEY")
    else:
        print("REBEL")
