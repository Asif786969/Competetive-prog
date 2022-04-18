import math
def calc(n):
    a=5*(x*x)-4
    a=math.sqrt(a)
    b=5*(x*x)+4
    b=math.sqrt(a)
    if(a%1==0 or b%1==0):
        return True
    else:
        return False
for _ in range(int(input())):
    n=int(input())
    if calc(n) is True:
        print("IsFibo")
    else:
        print("IsNotFibo")
