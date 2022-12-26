def merge(arr, temp, low, mid, high):
    i=low
    j=mid+1
    k=low
    c_inv=0
    while i<=mid and j<=high:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i=i+1
            k=k+1
        else:
            temp[k]=arr[j]
            c_inv = c_inv + (mid - i + 1)
            j=j+1
            k=k+1
    while i<=mid:
        temp[k]=arr[i]
        i=i+1
        k=k+1
    while j<=high:
        temp[k]=arr[j]
        j=j+1
        k=k+1

    for loop in range(low,high+1):
        arr[loop]=temp[loop]
    return c_inv



def _mergesort(arr, temp, low, high):
    c_inv=0
    if low<high:
        mid=(low+high)//2
        c_inv=c_inv+_mergesort(arr,temp,low,mid)
        c_inv=c_inv+_mergesort(arr,temp,mid+1,high)
        c_inv=c_inv+merge(arr,temp,low,mid,high)
    return c_inv



def mergesort(arr,n):
    temp=[0]*n
    return _mergesort(arr,temp,0,n-1)
arr=[1,20,6,4,5]
n=len(arr)
res=mergesort(arr,n)
print(res)