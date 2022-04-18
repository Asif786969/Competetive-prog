def sum_digit(a,s):
    if(a==0):
        return s
    d=a%10
    a=a//10
    s=d+sum_digit(a,s)
    return s

s=0
a=10642
print(sum_digit(a,s))
