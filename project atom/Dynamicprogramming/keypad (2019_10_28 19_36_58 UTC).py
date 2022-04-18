
def keypad(n):
    if n==0:
        A=[]
        A.append("")
        return A
    #calling recursion
    D={1:[""],2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
    A=keypad(n//10)
    r=n%10
    lis=D[r]
    new=[]
    #copying
    # for ele in A:
    #     new.append(ele)
    #combinations
    for char in lis:
        for ele in A:
            new.append(ele+char)
    return new
#n = int(input())

n=23
ans = keypad(n)
for s in ans:
    print(s)
