def checkMember(n):
    a=0
    b=1
    p=0
    while(a<=n):
        if(a!=n):
            t=b
            b=a+b
            a=t
        else:
            p=1
            break
    if(p==0):
        return 0
    else:
        return 1
n=6
if(checkMember(n)):
    print("true")
else:
    print("false")
