S="2$202200"
n=len(S)
Z=[0]*n
l=0
r=0
for i in range(n):
    if i<=r:
        Z[i]=min(r-i+1,Z[i-l])
    while(i+Z[i]<n and S[Z[i]]==S[i+Z[i]]):
        Z[i]+=1
    if (i+Z[i]-1)>r:
        l=i
        r=i+Z[i]-1
print(Z)
