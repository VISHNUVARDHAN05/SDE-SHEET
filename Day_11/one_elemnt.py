def one_element(arr):
    low=0
    high=len(arr)-2
    while low<=high:
        mid=(low+high)//2
        print(mid)
        if arr[mid]==arr[mid^1]:
            low=mid+1
        else:
            high=mid-1
    print(arr[low])
arr=[1,1,2,3,3,4,4]
one_element(arr)