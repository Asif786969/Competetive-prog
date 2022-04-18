def plandr(s,s2,i):
    l=len(s)
    l2=len(s2)
    if(l2==l):
        if(s==s2):
            print("true")
            return
        else:
            print("false")
            return
    s2+=s[l-1-i]
    i+=1
    plandr(s,s2,i)

s="racecar"
s2=""
i=0
plandr(s,s2,i)
