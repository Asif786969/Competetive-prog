for _ in range(int(input())):
    a=input()
    b=input()
    s=a+"$"+b+b[0:len(b)-1]
    p=len(a)
    n=len(s)
    Z=[0]*n
    l,r=0,0
    for i in range(1,n):
        if i>r:
            l,r=i,i
            while(r<n and s[r-l]==s[r]):
                r+=1
            Z[i]=r-l
            r-=1
        else:
            k=i-l
            if Z[k]<r-i-l:
                Z[i]=Z[k]
            else:
                l=i
                while(r<n and s[r-l]==s[r]):
                    r+=1
                Z[i]=r-l
                r-=1
    ans=0
    for i in range(1,n):
        if Z[i]==p:
            ans+=1
    print(ans)
