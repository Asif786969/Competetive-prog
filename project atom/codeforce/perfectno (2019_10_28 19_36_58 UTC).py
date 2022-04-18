import math
T=int(input())
for i in range(T):
    c,m,x=list(int(i) for i in input().split())
    if(c+m+x>=3 and c>=1 and m>=1):
        if(c>m):
            doublets=m
            leftc=c-m
            if(leftc+x>doublets):
                print(doublets)
            else:
                #filling the doublets
                count=leftc+x
                leftdoublets=doublets-count
                people=leftdoublets*2
                count+=people//3
                print(count)

        else:
            doublets=c
            leftm=m-c
            if(leftm+x>doublets):
                print(doublets)
            else:
                #filling the doublets
                count=leftm+x
                leftdoublets=doublets-count
                people=leftdoublets*2
                count+=people//3
                print(count)


    else:print(0)
