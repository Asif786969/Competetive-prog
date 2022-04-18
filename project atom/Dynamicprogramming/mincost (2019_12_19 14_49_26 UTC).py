for _ in range(int(input())):
    x=int(input())
    s=input()
    l=1
    while(l!=x):
        snew=s[0:l]
        rest=s[l:]
        count=int(snew[-1])
        for k in range(count):
            snew+=rest
        s=snew
        l+=1
    print(len(s))
