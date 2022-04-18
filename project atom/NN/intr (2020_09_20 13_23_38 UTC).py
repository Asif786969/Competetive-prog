from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
import random
J=1_000_000_007

###############################################################################\n=17
from collections import deque as D
Q=D()
Q.append([2,3])
Q.append([1,5])
x,y=Q.popleft()
print(x)
