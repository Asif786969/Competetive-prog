n=5
import math as M
def prime(n):
    i=2
    if n<2:
        return False
    else:
        for i in range(2,int(M.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
print(prime(9999999967))
