a={"apple":3,"hello":9,4:8}
print(a)
b=a.copy()
print(b)
print(a[4])
for i in a:
    print(i)
d = {1:2,"apple":5,"tree":7}
print(d.get(0,5))
d = {1:2,"abc":5,"def":7}
if 2 in d:
    print("Present")
else:
    print("Not Present")
