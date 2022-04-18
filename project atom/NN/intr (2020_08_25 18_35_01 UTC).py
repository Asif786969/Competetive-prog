A=[4,3,1,2]
print(A[A[0]-1])
t=A[0]
A[0]=A[t-1]
A[t-1]=t   
print(A)
