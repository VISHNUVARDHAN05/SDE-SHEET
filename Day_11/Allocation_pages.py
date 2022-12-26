def ispossible(arr,target,stu):
    s=1
    pages=0
    for i in range(len(arr)):
        if arr[i]>target:
            return False
        if pages+arr[i]>target:
            s=s+1
            pages=arr[i]
        else:
            pages=pages+arr[i]
    if s==stu:
        return True
    return False
def Allocation_pages(arr,stu):
    low=min(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        if ispossible(arr,mid,stu):
            high=mid-1
            res=mid
        else:
            low=mid+1
    return res

arr= [12, 34, 67, 90]
stu= 2
res=Allocation_pages(arr,stu)
print(res)