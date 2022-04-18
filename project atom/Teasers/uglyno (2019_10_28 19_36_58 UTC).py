#n=int(input())
n=15
u=0
i=1
def prmfac(u):
    if(u==1):
        return True
    f=0
    while(u!=1):
        if(u%2==0):
            u=u/2
        elif(u%5==0):
            u=u/5
        elif(u%3==0):
            u=u/3
        else:
            f=1
            break
    if(f==0):
        return True
    else:
        return False
while(i<=n):
    u+=1
    if(prmfac(u)==True):
        print(u)
        i+=1
