p=list(int(i) for i in input().split(" "))
n=p[0]
o=p[1]
a=[0]*n
for i in range(o):
    l=[]
    l=list(int(i) for i in input().split(" "))
    first=l[0]-1
    last=l[1]-1
    summand=l[2]
    for j in range(first,last+1,1):
        a[j]+=summand
print(max(a))
