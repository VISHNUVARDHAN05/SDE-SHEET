def longest_palindrome_substring(st):
    n = len(st)
    dp = [[0 for i in range(n)] for j in range(n)]
    max_len = 1
    i = 0
    while i < n:
        dp[i][i] = 1
        i = i+1
    i = 0
    s = i
    while i < n-1:
        if st[i] == st[i+1]:
            max_len = 2
            dp[i][i+1] = 1
            e = i+1
        i = i+1
    for i in range(3 , n+1):
        for j in range(n-i+1):
            k = i+j-1
            if st[j] == st[k] and dp[j+1][k-1] == 1:
                dp[j][k] = 1
                if i > max_len:
                    max_len = i
                    s = j
    print(st[s:s+max_len],max_len)
    return st[s:s+max_len]


st = "forgeeksskeegfor"
res = longest_palindrome_substring(st)
