def stock_span(arr,n,s):
    s[0]=1
    stack=[]
    stack.append(0)
    for i in range(1,n):
        while len(stack)!=0 and arr[i]>arr[stack[-1]]:
            stack.pop()
        if len(stack)==0:
            s[i]=i+1
        else:
            s[i]=i-stack[-1]
        stack.append(i)
    print(s)
price = [10, 4, 5, 90, 120, 80 ]
n = len(price)
s= [0] * (n)
stock_span(price,n,s)