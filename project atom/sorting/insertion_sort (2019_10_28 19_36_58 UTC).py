#insertion sort
a=[2,4,6,2,9,6,0]
n=7
for i in range(1,n):
    temp=a[i]
    j=i-1
    while(j>=0 and temp<a[j]):
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)
