def tower(n,S,H,E,i):
    if(n==1):
        print(S,E)
        return
    elif(n==0):
        return

    tower(n-1,S,E,H,i)
    print(S,E)
    tower(n-1,H,S,E,i)
tower(5,"a","b","c",i=0)
