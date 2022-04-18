def insert(a,i,ch):
    return a[0:i]+ch+a[i:]

def permutations(s):
    if(len(s)==0):
        return [""]
    A=permutations(s[1:])
    new=[]
    for ele in A:
        #placing the new character to all possible positions
        for i in range(len(ele)+1):
            st2=insert(ele,i,s[0])
            new.append(st2)
    return new


#s=input()
s="909"
li=permutations(s)
for ele in li:
    print(ele)
