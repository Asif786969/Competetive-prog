def fct(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return f
print(fct(26)-3*fct(23)+3*fct(20)-fct(17))
print(fct(5))
