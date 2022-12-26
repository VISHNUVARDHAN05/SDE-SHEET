def longest_common_subsequence(s1,s2):
    n1=len(s1)
    n2=len(s2)
    lcs=[[0 for i in range(n1+1)] for j in range(n2+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                lcs[i][j]=1+lcs[i-1][j-1]
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
    return lcs[n1][n2]


s1= "acd"
s2= "ced"
res=longest_common_subsequence(s1,s2)
print(res)