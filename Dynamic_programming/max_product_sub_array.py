def max_product_sub_array(arr):
    ans=arr[0]
    ma=ans
    mi=ans
    n=len(arr)
    for i in range(1,n):
        if arr[i]<0:
            ma,mi=mi,ma
        ma=max(ma*arr[i],arr[i])
        mi=min(arr[i],mi*arr[i])
        ans=max(ans,ma)
    return ans

arr=[1,2,-3,0,-4,-5]
res=max_product_sub_array(arr)
print(res)