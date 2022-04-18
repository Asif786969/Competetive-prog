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
s="abcdefabcde"
n=len(s)
hash=[0]*n
hash[0]=ord(s[i]-'a'+1)%MOD  
for i in range(n-1):
    hash[i+1]=(hash[i]+P[i]*(ord(s[i])-ord('a')+1))%MOD
print((hash[4])%MOD)
print((hash[10]-hash[6])%MOD)
