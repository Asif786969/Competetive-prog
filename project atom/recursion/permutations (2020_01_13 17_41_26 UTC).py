def insert(a,i,ch):
    return a[0:i]+ch+a[i:]

def permutations(s):
    if(len(s)==0):
        return [""]
    A=permutations(s[1:])
    new=[]
    for ele in A:
        for i in range(len(ele)+1):
            st2=insert(ele,i,s[0])
            new.append(st2)
    return new
s="123456789"
d=int(s[-1])
li=permutations(s)
# for ele in li:
#     print(ele)
if "391867254" in li:
    print("yes")
else:
    print("no")
A=[]
for str in li:
    i=1
    while(i<=d//2):
        a=str[0:i]
        b=str[i:d//2]
        c=str[d//2:]
        if a is '':
            a=0
        if b is '':
            b=0
        if c is '':
            c=0
        #print(a," ",b," ",c)
        if(int(a)*int(b)==int(c) or int(a)*int(c)==int(b) or int(b)*int(c)==int(a)):
            if int(c) not in A:
                A.append(int(c))
        i+=1
print(sum(A))
