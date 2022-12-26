def triplet_sum(arr):
    res=[]
    arr.sort()
    n=len(arr)
    print(arr)
    for i in range(n-1):
        if i==0 or (i>0 and arr[i]!=arr[i-1]):
            lo=i+1
            hi=n-1
            sum1=0-arr[i]
            while lo<hi:
                if arr[lo]+arr[hi]==sum1:
                    res.append([arr[i],arr[lo],arr[hi]])
                    while lo<hi and arr[lo]!=arr[lo+1]:
                        lo=lo+1
                    while lo<hi and arr[hi]!=arr[hi-1]:
                        hi=hi-1
                    lo=lo+1
                    hi=hi-1
                elif arr[lo]+arr[hi]>sum1:
                    hi=hi-1
                else:
                    lo=lo+1
    return res


arr = [-1,0,1,2,-1,-4]
res=triplet_sum(arr)
print(res)