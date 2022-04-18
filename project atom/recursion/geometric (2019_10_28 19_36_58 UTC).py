def geosum(k):
    if k==0:
        return 1
    sum=geosum(k-1)
    s=sum+1/(2**k)
    return s

k=10
s=0
l=geosum(k)
print("{0:.5f}".format(l))
