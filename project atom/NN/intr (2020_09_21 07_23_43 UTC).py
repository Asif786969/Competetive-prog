from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=1_000_000_007

###############################################################################\n=17
def R(n,k):
    if k<0:
        return 0
    if n==0:
        return 1
    if n<0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        if k>0:
            return 4
        else:
            return 3
    return R(n-1,k)+R(n-2,k)+R(n-3,k-1)

print(R(35,0))
