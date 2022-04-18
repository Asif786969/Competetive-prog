##n=int(input())
n=1532
b=a=n
x=0
while(n>0):
    x=x+1
    n=n//10
s=0
for i in range(1,x+1,1):
    r=a%10
    s+=r*(10**(x-i))
    a=a//10
if(b==s):
    print("palindrome")
else:
    print("not palindrome")
