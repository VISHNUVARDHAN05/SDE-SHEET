def merge(arr,low,mid,high):
    j=mid+1
    count=0
    for i in range(low,mid+1):
        while j<=high and arr[i]>=(2*arr[j]):
            j=j+1
        count=count+(j-(mid+1))
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left=left+1
        else:
            temp.append(arr[right])
            right=right+1
    while left<=mid:
        temp.append(arr[left])
        left=left+1

    while right<=high:
        temp.append(arr[right])
        right=right+1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    
    return count

def mergesort(arr,low,high):
    if low>=high:
        return 0
    mid=(low+high)//2
    inv=mergesort(arr,low,mid)
    inv=inv+mergesort(arr,mid+1,high)
    inv=inv+merge(arr,low,mid,high)
    return inv
def reverse_pair(arr):
    return mergesort(arr,0,len(arr)-1)
arr=[1,3,2,3,1]
res=reverse_pair(arr)
print(res)