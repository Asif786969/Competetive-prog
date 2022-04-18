x1,y1,x2,y2=list(int(i) for i in input().split(" "))
x3,y3,x4,y4=list(int(i) for i in input().split(" "))
x5,y5,x6,y6=list(int(i) for i in input().split(" "))
p1=0
p2=0
p3=0
p4=0
b1=0
b2=0
if((x1<=x4 and x3<=x1) and (y1<=y4 and y1>=y3)):
    p1=1
    b1+=1
if((x1<=x6 and x1>=x5) and (y1>=y5 and y1<=y6)):
    p1=1
    b2+=1
if((x2<=x4 and x3<=x2) and (y2<=y4 and y2>=y3)):
    p2=1
    b1+=1
if((x2<=x6 and x2>=x5) and (y2>=y5 and y2<=y6)):
    p2=1
    b2+=1
if((x1<=x4 and x3<=x1) and (y2<=y4 and y2>=y3)):
    p3=1
    b1+=1
if((x1<=x6 and x1>=x5) and (y2>=y5 and y2<=y6)):
    p3=1
    b2+=1
if((x2<=x4 and x3<=x2) and (y1<=y4 and y1>=y3)):
    p4=1
    b1+=1
if((x2<=x6 and x2>=x5) and (y1>=y5 and y1<=y6)):
    p4=1
    b2+=1
sum=p1+p2+p3+p4
if(b1==4 or b2==4):
    print("NO")
elif(sum==4):
    if(x1==x3==x5 and x4==x2==x6 and y5>y4):
        print("YES")
    elif(x1==x3==x5 and x4==x2==x6 and y5<=y4):
        print("NO")
    elif(x4>=x1 and x4<=x2 and x5>=x1 and x5<=x2 and x4>=x5):
        print("NO")
    elif(x4>=x1 and x4<=x2 and x5>=x1 and x5<=x2 and x4<x5):
        print("YES")
    elif(x6>=x1 and x6<=x2 and x3>=x1 and x3<=x2 and x6<x3):
        print("YES")
    elif(x6>=x1 and x6<=x2 and x3>=x1 and x3<=x2 and x6>=x3):
        print("NO")
    elif(y4>=y1 and y4<=y2 and y5>=y1 and y5<=y2 and y4<y5):
        print("YES")
    elif(y4>=y1 and y4<=y2 and y5>=y1 and y5<=y2 and y4>=y5):
        print("NO")
    elif(y3>=y1 and y3<=y2 and y6>=y1 and y6<=y2 and y6<y3):
        print("YES")
    elif(y3>=y1 and y3<=y2 and y6>=y1 and y6<=y2 and y6>=y3):
        print("NO")
    else:
        print("NO")
else:
    print("YES")
