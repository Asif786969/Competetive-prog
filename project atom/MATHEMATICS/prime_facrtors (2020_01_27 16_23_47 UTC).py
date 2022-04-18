import math
#n=971324893193
def primefactorisation(n):
	P=[]
	while(n%2==0):
		P.append(2)
		n//=2
	i=3
	while(i<=int(math.sqrt(n))):
		while(n%i==0):
			P.append(i)
			n//=i
		i+=2
	if(n>2):
		P.append(n)
	return P

A=primefactorisation(38)
print(A)
ans=1
count=1
for i in range(len(A)):
	if(i+1<len(A) and A[i]==A[i+1]):
		count+=1
	else:
		ans=ans*(count+1)
		count=1
print(ans)
