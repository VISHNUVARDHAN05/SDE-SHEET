def Trapping_rain_water_opt(arr):
    n=len(arr)
    left=0
    right=n-1
    res=0
    max_left=0
    max_right=0
    while left<=right:
        if arr[left]<=arr[right]:
            if arr[left]>max_left:
                max_left=arr[left]
            else:
                res=res+max_left-arr[left]
            left=left+1
        else:
            if arr[right]>max_right:
                max_right=arr[right]
            else:
                res=res+max_right-arr[right]
            right=right-1
    return res
def Trapping_rain_water(arr):
    n=len(arr)
    prev=[0]*n
    post=[0]*n
    prev[0]=arr[0]
    for i in range(1,n):
        prev[i]=max(prev[i-1],arr[i])
    post[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        post[i]=max(post[i+1],arr[i])
    res=0
    for i in range(n):
        res=res+min(prev[i],post[i])-arr[i]
    return res



arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res=Trapping_rain_water_opt(arr)
print(res)