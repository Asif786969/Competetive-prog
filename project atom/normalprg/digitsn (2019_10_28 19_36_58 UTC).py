H,n=list(int(i) for i in input().split(" "))
o=list(int(i) for i in input().split(" "))
#n open elevators
open=[0 for i in range(H)]
for ele in o:
    open[H-ele]=1
cystal=0
i=0

while(i<H):
    if(i+2<H):
        #jumping
        if(open[i]==1 and open[i+2]==1):
            i+=2
        #changing statsse
        elif(open[i]==1 and open[i+1]==1 and open[i+2]==0):
            cystal+=1
            i+=2
            open[i]==1
    elif(i+1<H):
        if(open[H]==1 and open[i+1]==0):
            i+=1
            open[i]=1
print(open)
print(cystals)
