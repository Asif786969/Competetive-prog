a=[]
n=10
for i in range(n):
    a.append(i)
for i in range(n-1):
    min=i
    for j in range(i+1,n,1):
        if(a[j]<a[min]):
            min=j
    a[i],a[min]=a[min],a[i]
print(a)
