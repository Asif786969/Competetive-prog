l,r=0,0
s=input()
n=len(s)
Z=[0]*n
for i in range(1,n):
    if s[0]=="0":
        break
    if s[i]=="0":
        continue
    if i>r:
        l,r=i,i
        while(r<n and s[r-l]==s[r]):
            r+=1
        Z[i]=r-l
        r-=1
    else:
        k=i-l
        if Z[k]<r-i+1:
            Z[i]=Z[k]
        else:
            l=i
            while(r<n and s[r-l]==s[r]):
                r+=1
            Z[i]=r-l
            r-=1
ans=0
for i in range(n//2+1):
    if Z[i]>0 and Z[i]>=i:
        ans+=1

print(ans)
print(Z[0:20])
