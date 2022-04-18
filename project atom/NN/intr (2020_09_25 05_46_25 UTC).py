from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=1_000_000_007

###############################################################################\n=17
def lunlun(i):
    s=str(i)
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1]))>1:
            return False
    return True
A=[]
for i in range(1,10**8):
    if lunlun(i):
        A.append(i)
print(len(A))
