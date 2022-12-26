def celebrity(arr):
    i=0
    n=len(arr)
    j=n-1
    while i<j:
        if arr[j][i]==1:
            j-=1
        else:
            i+=1
    celeb=i
    
    for i in range(n):
        if celeb!=i:
            if arr[celeb][i]==1 or arr[i][celeb]==0:
                return -1
    return celeb



n = 4
m = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
res=celebrity(m)
print(res)