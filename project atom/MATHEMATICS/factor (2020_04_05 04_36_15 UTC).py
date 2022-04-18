import math
def factors(n):
    A=[]
    i=1
    while(i<=math.sqrt(n)):
        if n%i==0:
            if (n//i)==i:
                A.append(i)
            else:
                A.append(i)
                A.append(n//i)
        i+=1
    return A
A=factors(1000000000000)
A.sort()
print(len(A))
