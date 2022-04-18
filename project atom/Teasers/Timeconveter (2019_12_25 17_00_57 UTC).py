import math as M
def F(theta,h,v):
    g=10
    b=(v**2)*(M.sin(2*theta))/(2*g) -(v*(M.cos(theta))/g)*(M.sqrt((v**2)*M.sin(theta)*M.sin(theta)+2*h*g))
    a=(v**2)*(M.sin(2*theta))/(2*g) +(v*(M.cos(theta))/g)*(M.sqrt((v**2)*M.sin(theta)*M.sin(theta)+2*h*g))
    return max(a,b)
for _ in range(int(input())):
    v,h,k=list(float(i) for i in input().split())
    v/=100
    h/100
    value=0
    theta=0
    while(theta<1.57):
        X=F(theta,h,v)
        if(X>value):
            value=X
        theta+=0.0001
    value*=100
    print(round(value**k)%(10**9+7))
