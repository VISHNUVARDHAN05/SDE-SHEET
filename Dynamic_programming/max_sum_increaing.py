def max_sum_increaing(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j] and dp[i]<dp[j]+arr[i]:
                dp[i] = dp[j] + arr[i]
    return max(dp)

arr=[9 ,1 ,2, 8 ]
res=max_sum_increaing(arr)
print(res)