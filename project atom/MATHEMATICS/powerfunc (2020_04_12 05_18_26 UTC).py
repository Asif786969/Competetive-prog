x=10**9+7
a,n=2,10
#n,m=list(int(i) for i in input().split())
def power(a,n):
    if n==0:
        return 1
    else:
        if(n%2==0):
            return ((power(a,n//2))**2)%x
        else:
            return ((a%x)*(((power(a,(n-1)//2)))**2)%x)%x

ans=power(2,10**9 + 5)
print(ans*3%x)
#THIS ONE HAS MINIMUM TIME COMPLEXITY O(log(n))
#SIMILARILY WE CAN CALCULATE x**n mod m by using mod m in every step
#MAKE SURE YOU USE (a.b)mod m=((a mod m)*(b mod m))*m
hello this is the third day when i am writing something that is useful and by the way this is just crazy for the well being of the party and i lost myself to what i am writing and
then certainly someone pops up to show the real place where i stand and by the way the way it looks it counts to be the the day when i was going to be slauteres
