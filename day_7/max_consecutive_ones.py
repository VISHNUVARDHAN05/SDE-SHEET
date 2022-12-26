def max_consecutive_ones(arr):
    max_c=0
    c=0
    for i in range(len(arr)):
        if arr[i]==0:
            c=0
        else:
            c=c+1
        max_c = max(max_c, c)
    return max(max_c,c)
arr = [1, 1, 0, 1, 1, 1]
res=max_consecutive_ones(arr)
print(res)