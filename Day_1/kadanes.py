def kadanes(l):
    sum1=0
    maxsum=0
    for i in range(len(l)):
        sum1=sum1+l[i]
        if sum1<0:
            sum1=0
        if sum1>maxsum:
            maxsum=sum1
    return maxsum
arr = [-2,1,-3,4,-1,2,1,-5,4]
res=kadanes(arr)
print(res)