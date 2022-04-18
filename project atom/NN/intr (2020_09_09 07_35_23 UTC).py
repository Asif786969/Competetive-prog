A=[0,26]
n=27
for i in range(1,10):
    A.append(A[-1]+A[-1]*26)
for i in range(len(A)):
    if A[i]>=n:
        break
l=i
s=""
print(l)

s=[]
if n==0:
    s=[0]
else:
    while(n):
        s.append((n%26))
        n//=26
s=s[::-1]
print(s)
L=len(s)
ans=s[L-l:]
print(ans)
real=""
for i in range(len(ans)):
    real+=chr(int(ans[i])+97)
print(real)
