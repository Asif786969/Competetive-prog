n=199
import math
def digitsum(x):
    s=0
    while(x>0):
        s+=x%10
        x//=10
    return s
maxi=1
d=50
p=int(n**((d-1)/d))
for a in range(p,n):
    for b in range(p,n):
        s=digitsum(a**b)
        if(s>maxi):
            maxi=s
print(maxi)
