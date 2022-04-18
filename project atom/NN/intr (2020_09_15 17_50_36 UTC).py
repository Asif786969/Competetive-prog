from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=int(1e9)+7

###############################################################################\n=17
from bisect import bisect_left as B
A=[1,4,6,7]
print(B(A,2))
