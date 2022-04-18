def phi1ton(n):
    phi=[0]*(n+1)
    phi[1]=1
    for i in range(2,n+1):
        phi[i]=i-1
    for i in range(2,n+1):
        for j in range(2*i,n+1,i):
            phi[j]-=phi[i]

    print(phi)


def phi2(n):
    phi=[0]*(n+1)
    phi[1]=1
    for i in range(2,n+1):
        phi[i]=i-1
    for i in range(2,n+1):
        if phi[i]==i:
            for j in range(i,n+1,i):
                phi[j]-=int(phi[j]/i)

    print(phi)

#n=int(input())
n=7
phi2(n)
phi1ton(n)
