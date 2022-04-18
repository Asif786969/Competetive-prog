def calculatepower(x):
    count=0
    while(x%2==0):
        x//=2
        count+=1
    return count
print(calculatepower(1440))
