n,k=list(int(i) for i in input().split())
rc,qc=list(int(i) for i in input().split())
Obs=[]
def queen(n,k,rc,qc,Obs):
    
for j in range(k):
    r,c=list(int(i) for i in input().split())
    Obs.append([r,c])
print(Obs)
queen(n,k,rc,qc,Obs)
