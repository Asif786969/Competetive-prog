from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=1_000_000_007

###############################################################################\n=17
d={1:3,-1:4}
x=sorted(d.keys())
print(x[1])