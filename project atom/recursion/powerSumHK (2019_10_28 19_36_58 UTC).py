def sumpower(S,P,num):
    if(num**P>S):
        return 0
    elif(num**P==S):
        return 1
    return sumpower(S,P,num+1)+sumpower(S-num**P,P,num+1)
print(sumpower(100,3,1))
