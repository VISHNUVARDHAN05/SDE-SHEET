def knapsack(n,weight,value,Wt):
    dp=[[0 for i in range(Wt+1)] for j in range(n+1)]
    for i in range(n+1):
        for wt in range(Wt+1):
            if i==0 or wt==0:
                dp[i][wt]=0
            elif weight[i - 1] <= wt:
                dp[i][wt] = max(value[i - 1]+ dp[i - 1][wt - weight[i - 1]], dp[i - 1][wt])
            else:
                dp[i][wt]=dp[i-1][wt]
    print(dp)

n=4
weight=[1, 2, 4, 5]
value=[5, 4, 8, 6]
Wt=5
knapsack(n,weight,value,Wt)