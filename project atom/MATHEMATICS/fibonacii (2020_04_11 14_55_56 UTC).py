#the best fibonacci
import math as M
import sys
sys.setrecursionlimit(10**6)
def fibonacii(n):
    return fib(n)[0]
e=10**20+7
def fib(n):
    if n==0:
        return 0,1
    else:
        a,b=fib(n//2)
        c=a*(2*b-a)
        d=a**2+b**2
        c=c%e
        d=d%e
        if n%2==0:
            return c,d
        else:
            return d,(c+d)%e
n=100
print(M.log10(fibonacii(n)))
