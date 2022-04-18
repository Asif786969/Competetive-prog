s="efiddakofhuycqedcnduv"
stack=[]
lastpop=""
for c in s:

    print(stack)
    if stack:
        if c==lastpop:
            continue
        if c==stack[-1]:
            lastpop=c
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)
print(stack)
