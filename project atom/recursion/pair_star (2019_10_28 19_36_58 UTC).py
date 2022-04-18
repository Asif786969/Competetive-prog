def con(s,g,i,p):
    if(len(s)==i):
        return g
    if(g[p]==s[i]):
        g+="*"
        p+=1
    else:
        g+=s[i]
        i+=1
        p+=1
    return con(s,g,i,p)

print(con("cicvvbllllnbbnnn","c",1,0))
