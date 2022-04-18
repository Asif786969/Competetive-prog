for _ in range(int(input())):
    n,c=list(int(i) for i in input().split())
    A=list(int(j) for j in input().split())
    friends=[]
    for k in range(n):
        s=list(int(i) for i in input().split())
        friends.append(s[1:])
    print(friends)
    
