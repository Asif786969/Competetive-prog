n=int(input())
b=[]
for i in range(n):
    a=[]
    a=list(int(i) for i in input().split(" "))
    b.append(a)

d1=0
d2=0
for i in range(n):
    for j in range(n):
        if(i==j):
            d1+=b[i][j]
        elif(i+j==n-1):
            d2+=b[i][j]
        if(i==j and i+j==n-1):
            d2+=b[i][j]
print(abs(d1-d2))
    
