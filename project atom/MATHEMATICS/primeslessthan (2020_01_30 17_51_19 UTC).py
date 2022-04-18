n=10
import math as M
def calc(n):
    B=[False for i in range(n+1)]
    for i in range(2,n):
        if B[i] is False:
            ele=i
            count=2
            while(ele<=n):
                ele=ele*count
                if(ele<=n):
                    B[ele]=True
                count+=1
    A=[]
    for i in range(2,len(B)):
        if B[i] is False:
            A.append(i)
    #print(A)
print(calc(10**7))
