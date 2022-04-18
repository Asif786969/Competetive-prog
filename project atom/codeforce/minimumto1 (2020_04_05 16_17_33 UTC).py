n,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
A.sort()
sum=0
for i in range(n-1,-1,-1):
    sum+=(i*A[i]-(n-1-i)*A[i])**k
print(sum)
