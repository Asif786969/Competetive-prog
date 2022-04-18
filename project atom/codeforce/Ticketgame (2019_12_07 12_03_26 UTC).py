A=[15,15,14,14,13,13,12,12,11,11,11,11,11,10,10,10,10,10,10,10,10,9,8,7,7]
n=len(A)
print(n)
g=s=b=0
max=n//2
if max<5:
    print(0," ",0," ",0)
else:
    gmax=(max-2)//3
    countgold=1
    countsilver=1
    countbronze=1
    for i in range(gmax):
        if(A[i]==A[i+1]):
            countgold+=1
        else:
            break
    if(A[countgold-1]==A[gmax]):
        print(0," ",0," ",0)
    else:
        if(max-countgold>2*(countgold+1)):
            #for silver and bronze
            sind=countgold
            for j in range(countgold,max-countgold):
                if(j+1<max and A[j]>=A[j+1]):
                    countsilver+=1
                if(countsilver>countgold):
                    break
            if(A[countsilver+countgold-1]==A[countgold+countsilver]):
                extra=0
                k=countsilver+countgold-1
                while(k+1<max and A[k]==A[k+1]):
                    extra+=1
                    k+=1
                #print(extra," ",countsilver)
                countsilver+=extra
            countbronze=max-countgold-countsilver
            if(countgold<countbronze and countgold<countsilver):
                redbrz=0
                if(A[max]==A[max-1]):
                    redbrz=1
                    t=max-1
                    while(t>0 and A[max-1]==A[t-1]):
                        redbrz+=1
                        t-=1
                countbronze-=redbrz
                if(countbronze>countgold):
                    print(countgold," ",countsilver," ",countbronze)
                else:
                    print(0," ",0," ",0)
            else:
                print(0," ",0," ",0)
        else:
            print(0," ",0," ",0)
