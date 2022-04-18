from cmath import exp,pi
import math as M
def dft(A,inv):
    n=len(A)
    if n==1:
        return
    Ao=[0]*(n//2)
    A1=[0]*(n//2)
    i=0
    j=0
    while(i<n):
        Ao[j]=A[i]
        A1[j]=A[i+1]
        i+=2
        j+=1
    dft(Ao,inv)
    dft(A1,inv)
    ang=((2*pi)/n)*(-1)
    if inv is False:
        ang*=-1
    w=1
    #print(ang)
    a=M.cos(ang)
    c=M.sin(ang)
    wn=a+1j*c
    for i in range(n//2):
        A[i]=Ao[i]+w*A1[i]
        A[i+n//2]=Ao[i]-w*A1[i]
        if inv:
            A[i]/=2
            A[i+n//2]/=2
        w*=wn
A=[2,3,0,0]
B=[4,1,1,0]
dft(A,False)
dft(B,False)
print(A)
print(B)
for i in range(len(A)):
    A[i]*=B[i]
dft(A,True)
print(*(A))
