l,r=0,0
s=""
for i in range(10**5):
    s+="a"
n=len(s)
Z=[0]*n
for i in range(n):
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
