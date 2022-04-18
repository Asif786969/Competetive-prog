n=int(input())
A=list(int(i) for i in input().split())
#n=5
#A=[-5,-3,5,3,0]
moves=0
#z represent no of zero,u posi,v neg
z=0
u=0
v=0
for ele in A:
    if ele==0:
        z+=1
    if ele<=-1:
        moves+=abs(ele)-1
        v+=1
    if ele>=1:
        moves+=ele-1
        u+=1
moves+=z
if(z==0):
    if v%2!=0:
        moves+=2
print(moves)
