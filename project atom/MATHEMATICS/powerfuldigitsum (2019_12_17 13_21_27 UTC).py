A=[2,5,7]
for i in range(1,3):
    x=abs(A[i]-A[i-1])
    y=abs(A[i]-1)
    w=abs(A[i-1]-1)
    if(max(x,y,w) is y):
        A[i-1]=1
    elif(max(x,y,w) is w):
        A[i]=1
print(A)
