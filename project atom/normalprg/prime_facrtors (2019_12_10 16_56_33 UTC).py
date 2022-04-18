import math
n=1000000
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

A=primefactorisation(n)
print(A)
