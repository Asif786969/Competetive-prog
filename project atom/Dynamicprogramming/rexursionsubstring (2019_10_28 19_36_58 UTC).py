def substring(s):
    if len(s)==0:
        A=[]
        A.append("")
        return A
    smallstr=s[1:]
    B=substring(smallstr)
    ch=s[0]
    new=[]
    for ele in B:
        new.append(ele)
    for ele in B:
        new.append(s[0]+ele)
    return new
s="abcd"
print(substring(s))
