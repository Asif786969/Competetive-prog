def convert(s,i,p):
    l=len(s)
    if(l==0):
        return i
    a=int(s[l-1])
    x=s[0:l-1]
    i+=a*(10**p)
    p+=1
    d=convert(x,i,p)
    return d
print(convert("544",0,0))
