from sys import setrecursionlimit as SET
SET(10**6)
def permutations(s):
    if len(s)==1:
        return [s]
    ele=s[0]
    A=permutations(s[1:])
    x=[]
    for i in range(len(A)):
        for j in range(len(A[i])+1):
            ans=""
            ans+=A[i][0:j]+ele+A[i][j:]
            x.append(ans)
    return x

#s=input()
s="1234"
a=permutations(s)
for e in a:
    print(e)
