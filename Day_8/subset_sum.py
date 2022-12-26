def subset_sum(arr,ind,sum1,n,l):
    if ind==n:
        l.append(sum1)
        return
    subset_sum(arr, ind+1, sum1+arr[ind], n, l)
    subset_sum(arr, ind+1, sum1, n, l)
    pass


arr=[1,2,3]
n=len(arr)
l=[]
res=subset_sum(arr,0,0,n,l)
l.sort()
print(l)