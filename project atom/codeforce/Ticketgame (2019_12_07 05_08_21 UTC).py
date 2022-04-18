#n=int(input())
#A=list(int(i) for i in input().split(" "))
n=31
A=[64,64,63,58,58,58,58,58,37,37,37,37,34,34,28,28,28,28,28,28,24,24,19,17,17,17,17,16,16,16,16,11]
g=s=b=0
max=n//2
if max<5:
    print(0," ",0," ",0)
else:
    gmax=(max-2)//3
    countgold=1
    countsilver=1
    countbronze=1
    bool=True
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
                if(A[j]>=A[j+1]):
                    countsilver+=1
                if(countsilver>countgold):
                    break
            if(A[countsilver+countgold-1]==A[countgold+countsilver]):
                extra=0
                k=countsilver+countgold
                while(A[k]==A[k+1]):
                    extra+=1
                countsilver+=extra
            countbronze=max-countgold-countsilver
            if(countgold<countbronze and countgold<countsilver):
                print(countgold," ",countsilver," ",countbronze)
            else:
                print(0," ",0," ",0)
        else:
            print(0," ",0," ",0)
