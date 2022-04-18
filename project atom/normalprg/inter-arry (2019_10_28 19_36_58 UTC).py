#Makes out the interdection of 2 arrays without using inbuilt sets functions
n=7
A=[2,3,3,6,6,1,0]
m=5
B=[1,3,3,3,1]
#intersection should be =[1,3,3,5]
for i in range(n):
    r=A[i]
    for j in range(m):
        if(r==B[j]):
            print(r)
            B[j]="a"
            break
