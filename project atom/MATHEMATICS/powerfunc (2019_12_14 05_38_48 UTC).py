def power(a,n):
    if n==0:
        return 1
    else:
        if(n%2==0):
            return (power(a,n//2))**2
        else:
            return a*((power(a,(n-1)//2))**2
print(power(10,3))
#THIS ONE HAS MINIMUM TIME COMPLEXITY O(log(n))
#SIMILARILY WE CAN CALCULATE x**n mod m by using mod m in every step
#MAKE SURE YOU USE (a.b)mod m=((a mod m)*(b mod m))*m
