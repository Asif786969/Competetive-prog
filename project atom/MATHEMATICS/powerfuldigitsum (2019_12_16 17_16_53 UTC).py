n=18
def digitsum(x):
    s=0
    while(x>0):
        s+=x%10
        x//=10
    return s
maxi=1
for a in range(1,n):
    for b in range(1,n):
        s=digitsum(a**b)
        if(s>maxi):
            maxi=s
print(maxi)
