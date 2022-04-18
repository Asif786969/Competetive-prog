#ENTER THE EQUATION
#s=input()
def checkwhetherexist(c,g):
    if(c%g):
        return False
    else:
        return
def gcd(a,b):
    q=a//b
    r=a%b
    if(r==0):
        return b
    else:
        return gcd(b,r)

a,b,c=list(int(i) for i in input().split(" "))
if(abs(a)>abs(b)):
    g=gcd(abs(a),abs(b))
else:
    g=gcd(abs(b),abs(a))
xg,yg=checkwhetherexist(c,g)
x0=(xg*c)//g
y0=(yg*c)//g
#all solutions
for k in range(10):
    x=x0+(b*k)//g
    y=y0-(a*k)//g
    print(x," ",y)















all
