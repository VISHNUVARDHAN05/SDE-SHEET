#arr=[1, 2, 8, 4, 9]
def ispossible(arr,s,n_c,mid):
    stall_count=1
    place=arr[0]
    for i in range(1,s):
        if (arr[i]-place)>=mid:
            stall_count=stall_count+1
            place=arr[i]
        if stall_count==n_c:
            return True
    return False
def Aggressive_cows(arr,n_c,stalls):
    low=1
    high=arr[stalls-1]-arr[0]
    res=0
    while low<=high:
        mid=(low+ high)//2
        if ispossible(arr,stalls,n_c,mid):
            res=mid
            low=mid+1
        else:
            high=mid-1
    print(res)
arr=[1, 2, 4, 8, 9]
n_c=3
stalls=5
Aggressive_cows(arr,n_c,stalls)