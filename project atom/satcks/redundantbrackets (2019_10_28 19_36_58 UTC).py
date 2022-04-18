

def checkRedundant(string):
    stack=[]
    c=-1
    for ele in string:
        if(ele is not ")"):
            stack.append(ele)
        else:
            c=0
            while(stack[-1] is not "("):
                stack.pop()
                c+=1
    if(c==-1):
        return False
    if(c==0):
        return True
    else:
        return False
#string = input()
string="a+b"
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')
