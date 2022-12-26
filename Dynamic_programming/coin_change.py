def solver(n,m,coins,dp):
    if m==0:
        return (n%coins[m]==0)
    if n<0:
        return 0
    if n==0:
        return 1

    if dp[m][n] != -1:
        return dp[m][n]
    t=solver(n-coins[m],m,coins,dp)
    nt=solver(n,m-1,coins,dp)
    dp[m][n]=t+nt
    return t+nt
def solve(n,coins):
    m=len(coins)
    dp=[[0 for i in range(n+1)] for j in range(m)]
    for i in range(1,n+1):
        if i%coins[0]==0:
            dp[0][i]=i%coins[0]
    for i in range(1,m):
        for j in range(1,n+1):
            t=0
            if coins[i]<=j:
                t=dp[i][j-coins[i]]
            nt=dp[i-1][j]
            dp[i][j]=t+nt

    print(dp)
    return solver(n,m-1,coins,dp)
n=4
coins=[1,2,3]
x=solve(n,coins)
print(x)