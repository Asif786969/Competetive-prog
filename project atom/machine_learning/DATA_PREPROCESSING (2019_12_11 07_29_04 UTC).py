t=1
import math
for i in range(t):
    n=10001
    count=2
    p=2
    i=2
    x=4
    Prime=[2,3]
    if(n<=2):
        print(Prime[n-1])
    else:
        if(len(Prime)>=n):
            print(Prime[n-1])
        else:
            while(count!=n):
                flag=True
                for a in range(count):
                    if(x%Prime[a]==0):
                        flag=False
                        break
                if flag is True:
                    Prime.append(x)
                    count+=1
                x+=1
        print(Prime[-1])
        print(*Prime)
