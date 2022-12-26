def search_rotated(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if target>=arr[low] and target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target>=arr[mid] and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1

    return -1
arr=[4,5,6,7,0,1,2]
target=0
res=search_rotated(arr,target)
print(res)