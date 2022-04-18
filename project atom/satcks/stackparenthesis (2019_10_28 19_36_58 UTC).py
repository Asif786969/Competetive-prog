def paranthesis(s):
    A=[]
    for char in s:
        if(char in "{(["):
            A.append(char)
        elif(char is "}"):
            if(not A or A[-1]!="{"):
                return False
            A.pop()
        elif(char is ")"):
            if(not A or A[-1]!="("):
                return False
            A.pop()
        elif(char is "]" ):
            if(not A or A[-1]!="["):
                return False
            A.pop()
    if(not A):
        return True
    else:
        return False

s=input()
paranthesis(s)
