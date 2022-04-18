#n=int(input())
#s=input()
n=60
s="(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))"
first=0
second=0
def move(st,n):
    new=""
    new+=st[-1]
    for i in range(n-1):
        new+=st[i]
    return new
def swap(st,i,j):
    new=list(st)
    new[i],new[j]=new[j],new[i]
    p=""
    for ele in new:
        p+=ele
    return p

def checkbalnce(a):
    stack=[]
    for ch in a:
        if(ch in "("):
            stack.append(ch)
        else:
            if(len(stack)!=0):
                stack.pop()
            else:
                return False


    if(len(stack)==0):
        return True
    else:
        return False
max=0
for i in range(n):
    for j in range(n):
        if(s[i]!=s[j]):
            st=swap(s,i,j)
        else:
            st=s
        count=0
        for k in range(n):
            if(checkbalnce(st) is True):
                count+=1
            st=move(st,n)
        if(count>max):
            max=count
            first=i
            second=j

print(max)
print(first+1," ",second+1)
