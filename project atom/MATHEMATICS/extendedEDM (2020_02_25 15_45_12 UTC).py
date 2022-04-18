#Python program for Extended Euclidean algorithm
def egcd(a,b):
	if a == 0:
		return (b,0,1)
	else:
		gcd,x,y=egcd(b%a,a)
		return (gcd,y-(b//a)*x,x)

gcd,x,y=egcd(30,5)
print(gcd, x, y)
