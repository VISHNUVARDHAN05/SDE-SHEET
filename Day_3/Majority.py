def Majority(arr):
    c=0
    i=0
    ele=0
    while i<len(arr):
        if c==0:
            ele=arr[i]
        if ele==arr[i]:
            c=c+1
        else:
            c=c-1
        i=i+1
    return ele


arr=[2,2,1,1,1,2,2]
res=Majority(arr)
print(res)