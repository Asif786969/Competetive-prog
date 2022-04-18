#str=input()
str="apple is as good as banana"
li=[1,4,6,6,7,7,1,1,1]
a={}
for ele in li:
    if ele in a:
        a[ele]+=1
    else:
        a[ele]=1
print(a)
max=0
for ele in a:
    if(a[ele]>max):
        max=a[ele]
        key=ele
print(max)
print(key)
