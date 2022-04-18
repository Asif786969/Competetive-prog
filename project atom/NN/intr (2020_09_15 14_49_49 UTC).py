from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=int(1e9)+7

###############################################################################\n=17
def sum(n):
    a=0
    while(n):
        a+=n%10
        n//=10

    return a
print(sum(217871987498122))
