def binary(x):
    ans=""
    while(x>0):
        ans=str(x%2)+ans
        x//=2
    return ans
print(binary(7))
