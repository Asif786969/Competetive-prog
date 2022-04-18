import math as M
def Karasuba(x,y):
    if x<10 and y<10:
        return x*y
    n=max(len(str(x)),len(str(y)))
    p=M.ceil(n/2)
    D=10**p
    X_h=x//D
    X_l=x%D
    Y_h=y//D
    Y_l=y%D
    S1=Karasuba(X_h,Y_h)
    S2=Karasuba(X_l,Y_l)
    S3=Karasuba(X_h+X_l,Y_h+Y_l)
    S4=S3-S2-S1
    return int(S1*(D**2)+S4*D+S2)
n=n=10**(10**5)
print(Karasuba(12,34))
