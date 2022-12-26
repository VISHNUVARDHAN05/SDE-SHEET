def edit_distance(s1,s2):
    n1=len(s1)
    n2=len(s2)
    lcs=[[0 for i in range(n1+1)] for j in range(n2+1)]
    for i in range(n1+1):
        lcs[0][i]=i
    for j in range(n2+1):
        lcs[j][0]=j

    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if s1[j-1]==s2[i-1]:
                lcs[i][j]=lcs[i-1][j-1]
            else:
                lcs[i][j]=1+min(lcs[i-1][j],min(lcs[i][j-1],lcs[i-1][j-1]))
    return lcs[n2][n1]


s1= "horse"
s2= "ros"
res=edit_distance(s1,s2)
print(res)