def unique_paths(rows,cols):
    dp=[[0 for i in range(cols)] for j in range(rows)]
    for i in range(cols):
        dp[i][0]=1
    for i in range(rows):
        dp[0][i]=1
    for i in range(1,rows):
        for j in range(1,cols):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[rows-1][cols-1]


rows=3
cols=3
res=unique_paths(rows,cols)
print(res)