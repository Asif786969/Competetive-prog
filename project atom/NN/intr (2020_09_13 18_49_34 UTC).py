from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=int(1e9)+7

###############################################################################\n=17
X=[False]*(1000000)
P=[]
for i in range(2,len(X)):
    if X[i] is False:
        for j in range(2*i,len(X),i):
            X[j]=True
for i in range(2,len(X)):
    if X[i] is False:
        P.append(i)
print(len(P))
print(M.gcd(0,1))
