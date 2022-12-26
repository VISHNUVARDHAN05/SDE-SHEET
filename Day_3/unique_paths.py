def unique_paths(m,n,i,j):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n:
        return 0

    return unique_paths(m,n,i+1,j)+unique_paths(m,n,i,j+1)

def unique_paths_comb(m,n):
    M=m+n-2
    N=m-1
    res=1
    for i in range(1,n+1):
        res=res*((M-N+1)//i)
    return res
m=2
n=3
res=unique_paths_comb(m,n)
print(res)