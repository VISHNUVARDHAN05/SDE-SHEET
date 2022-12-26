def min_path_sum_in_grid(grid):
    rows=len(grid)
    cols=len(grid[0])
    dp=grid.copy()
    for i in range(1,rows):
        dp[0][i]=dp[0][i-1]+dp[0][i]
    for j in range(1,cols):
        dp[i][0]=dp[i-1][0]+dp[i][0]
    for i in range(1,rows):
        for j in range(1,cols):
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]
    print(dp)




grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
min_path_sum_in_grid(grid)