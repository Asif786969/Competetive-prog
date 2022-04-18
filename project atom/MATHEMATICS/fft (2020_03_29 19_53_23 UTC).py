from cmath import exp,pi
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

# print( ' '.join("%5.3f" % f
#                 for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])) )
def iFFT(A):
    n = len(A)
    A = fft([a.conjugate() for a in A])
    return [a.conjugate()/n for a in A]

A1=fft([1,2])
print(A1)
B2=fft([3,4])
print(B2)
C=[]
for i in range(2):
    C.append(A1[i]*B2[i])
print(iFFT(C))
