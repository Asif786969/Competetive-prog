def SieveOfEratosthenes(n):
    prime=[True for i in range(n+1)]
    p=2
    sum=0
    while(p*p<=n):
        if (prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n+1):
        if prime[p]:
            sum+=p
    print(sum)
SieveOfEratosthenes(0)
