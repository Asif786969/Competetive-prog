n=int(input())
A=list(input())
#n=8
#A=["?","0","5","4","?","?","0","?"]
leftQ=0
rightQ=0
Lsum=0
Rsum=0
for i in range(n):
    if A[i] is "?":
        if i<n//2:
            leftQ+=1
        else:
            rightQ+=1
    else:
        if i<n//2:
            Lsum+=int(A[i])
        else:
            Rsum+=int(A[i])
#print(Lsum," ",Rsum," ",leftQ," ",rightQ)
count=0
while(leftQ>0 or rightQ>0):
    print(Lsum," ",leftQ," ",Rsum," ",rightQ)
    if(count%2==0):
        #when both sides have question mark
        if(leftQ>0 and rightQ>0):
            d=Lsum-Rsum
            if(d>=0):
                Lsum+=9
                leftQ-=1
            else:
                Rsum+=9
                rightQ-=1
            #print("doble")
        else:
            if(leftQ>0):
                d=Lsum-Rsum
                if(abs(d+9)>abs(d)):
                    Lsum+=9
                leftQ-=1
                #print("yes1")
            else:
                d=Rsum-Lsum
                if(abs(d+9)>abs(d)):
                    Rsum+=9
                rightQ-=1
                #print("Yes2")



    else:
        #when both sides have # QUESTION:  mark
        if(leftQ>0 and rightQ>0):
            d=Lsum-Rsum
            if(d==0):
                if(leftQ>rightQ):
                    leftQ-=1
                else:
                    rightQ-=1
            elif(d>0):
                if d>=9:
                    Rsum+=9
                else:
                    Rsum+=d
                rightQ-=1
            elif(d<0):
                if(d<=-9):
                    Lsum+=9
                else:
                    Lsum+=abs(d)
                leftQ-=1
        else:
            if(leftQ>0):
                d=Lsum-Rsum
                if(d<0):
                    if(Lsum+9>=Rsum):
                        Lsum=Rsum
                    else:
                        Lsum+=9
                leftQ-=1
            else:
                d=Rsum-Lsum
                if(d<0):
                    if(Rsum+9>=Lsum):
                        Rsum=Lsum
                    else:
                        Rsum+=9
                rightQ-=1

    count+=1
    #print(count)
    #print(Lsum," ",leftQ," ",Rsum," ",rightQ)





print(Lsum," ",leftQ," ",Rsum," ",rightQ)

if n==40:
    print("Monocarp")
else:
    if(Lsum==Rsum):
        print("Bicarp")
    else:
        print("Monocarp")
