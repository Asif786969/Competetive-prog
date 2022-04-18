from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
MOD=10**9+7
#=======================================================
p=31
P=[1]*10**5
for i in range(1,10**5):
    P[i]=(P[i-1]*p)%MOD
s="abab"
n=len(s)
hash=[0]*(n+1)
for i in range(n):
    hash[i+1]=(hash[i]+P[i]*(ord(s[i])-ord('a')+1))%MOD
print(hash)
print((hash[4]-hash[2]+MOD)%MOD)
