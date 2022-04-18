def spiralPrint(a,m,n):
    #row top to bottom
    k=0
    while(a[m//2][n//2]!="a"):
        if(k%4==0):
            for i in range(m):
                for j in range(n):
                    if(a[i][j]!="a"):
                        print(a[i][j],end=" ")
                        a[i][j]="a"
            k+=1

        elif(k%4==1):
            for j in range(n-1,-1,-1):
                for i in range(m):
                    if(a[i][j]!="a"):
                        print(a[i][j],end=" ")
                        a[i][j]="a"
            k+=1

    #row from bottom to top
        elif(k%4==2):
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if(a[i][j]!="a"):
                        print(a[i][j],end=" ")
                        a[i][j]="a"
            k+=1

    #column from left
        elif(k%4==1):
            for j in range(n):
                for i in range(m-1,-1,-1):
                    if(a[i][j]!="a"):
                        print(a[i][j],end=" ")
                        a[i][j]="a"
            k+=1


#Main
arr=[[1,2,3],[4,5,6],[7,8,9]]
m=3
n=3
spiralPrint(arr,m,n)
