def stockSpan(price,n):
    stack=[]
    count=1
    span=[1]
    for i in range(1,len(price)):
        while(len(stack)>0 and price[i]>price[stack[-1]]):
                stack.pop()
                count+=1
            if(price[i]<=price[stack[-1]]):
                count=1
                stack.append(i)
            else:
                stack.append(i)
            print(count,end=" ")

#n = int(input())
#price = [int(ele) for ele in input().split()]
n=6
price=[4,3,5,6,7,5]
stockSpan(price,n)
