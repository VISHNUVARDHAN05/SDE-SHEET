def compute_lps(s,lps,n):
    i=1
    j=0
    while i<n:
        if s[i]==s[j]:
            j = j + 1
            lps[i]=j
            i=i+1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                lps[i]=0
                i=i+1

def min_inserions_palindrome(s):
    res=s+"$"+s[::-1]
    n = len(res)
    lps=[0]*n
    compute_lps(res,lps,n)
    print(len(s)-lps[-1])
s="AACECAAAA"
min_inserions_palindrome(s)