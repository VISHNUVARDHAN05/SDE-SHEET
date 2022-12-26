def remove_duplicates(arr):
    i=0
    n=len(arr)
    for j in range(1,n):
        if arr[j]!=arr[i]:
            i=i+1
            arr[i]=arr[j]
    return i+1

arr=[1,1,2,2,2,3,3,4,5]
res=remove_duplicates(arr)
print(arr)
print(res)