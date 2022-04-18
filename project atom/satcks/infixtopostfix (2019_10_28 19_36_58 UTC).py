#This one is without brackets
stack=[]
def hasHigher(exp1,exp2):
    if(exp1=="^"):
        t1=3
    elif(exp1=="*"):
        t1=2.5
    elif(exp1=="/"):
        t1=2
    elif(exp1=="+"):
        t1=1.5
    elif(exp1=="-"):
        t1=1
    if(exp2=="^"):
        t2=3
    elif(exp2=="*"):
        t2=2.5
    elif(exp2=="/"):
        t2=2
    elif(exp2=="+"):
        t2=1.5
    elif(exp2=="-"):
        t2=1

    if(t1>t2):
        return True
    else:
        return False


string="A+B*C-D*E"
res=""
for char in string:
    if(char in "*-+/^"):
        while(len(stack)!=0 and hasHigher(stack[-1],char)):
            res+=stack[-1]
            stack.pop()
        stack.append(char)
    else:
        res+=char
while(len(stack)!=0):
    res+=stack[-1]
    stack.pop()
print(res)
