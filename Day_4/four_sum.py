def four_sum(arr,target):
    d={}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            d[arr[i]+arr[j]]=[i,j]

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if target-arr[i]-arr[j] in d:
                x=d[target-arr[i]-arr[j]]
                if x[0]!=i and x[0]!=j and x[1]!=i and x[1]!=j:
                    return True

    return False

arr=[1,2,3,4,5]
res=four_sum(arr,10)
print(res)