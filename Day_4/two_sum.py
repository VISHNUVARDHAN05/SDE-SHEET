def two_sum(arr,target):
    d={}
    for i in arr:
        d[i]=True
    for i in arr:
        if target-i in d:
            return True
    return False

arr=[1,2,3,4,5]
res=two_sum(arr,5)
print(res)