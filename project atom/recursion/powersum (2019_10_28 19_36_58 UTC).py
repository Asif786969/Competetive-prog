import math
S=100
P=3
ways=0
def sum(arr):
    sums=0
    for ele in arr:
        sums+=ele
    return sums
def powersum(S,ways):
    if(S==0):
        return [[0]]
    #including i**2
    root=int(math.sqrt(S))
    for i in range(1,root+1):
        partial=powersum(S-i**2,ways)
        for ele in partial:
            if(i**2+sum(ele)==S):
                ways+=1
    return partial


dp=[-1 for i in range(101)]
print(powersum(100,0))
