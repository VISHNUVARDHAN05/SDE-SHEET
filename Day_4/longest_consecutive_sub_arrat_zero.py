def longest_consecutive_sub_arrat_zero(arr,n):
    d={}
    maxi=0
    sum1=0
    for i in range(len(arr)):
        sum1=sum1+arr[i]
        if sum1==0:
            maxi=i+1
        else:
            if sum1 in d:
                maxi=max(maxi,i-d[sum1])
            else:
                d[sum1]=i
    return maxi

n = 6
arr = [9, -3, 3, -1, 6, -5]
res=longest_consecutive_sub_arrat_zero(arr,n)
print(res)