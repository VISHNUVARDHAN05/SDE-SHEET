def longest_substring(s):
    n=len(s)
    left=0
    right=0
    d={}
    length=0
    for i in range(len(s)):
        if s[i] in d:
            left=max(left,1+d[s[i]])
        length=max(length,i-left+1)
        d[s[i]]=i
    return length


s="GEEKSFORGEEKS"
res=longest_substring(s)
print(res)