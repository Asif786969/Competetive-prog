s="12:00:00PM"
a=s.split(":")
hr=a[2][2:4]
if(hr=="PM" and a[0]!="12"):
    print(int(a[0])+12,end=":")
elif(hr=="PM" and a[0]=="12"):
    print(a[0],end=":")
elif(hr=="AM" and a[0]=="12"):
    print(int(a[0])-12,end="0:")
else:
    print(a[0],end=":")
print(a[1],end=":")
print(a[2][0:2])
