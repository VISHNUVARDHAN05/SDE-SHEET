def lis(arr):
    n=len(arr)
    lis=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j] and lis[i]<lis[j]+1:
                lis[i] =lis[j] + 1
    return max(lis)

arr=[5 ,4 ,11 ,1 ,16, 8]
res=lis(arr)
print(res)