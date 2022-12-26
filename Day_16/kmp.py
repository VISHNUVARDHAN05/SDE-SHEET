def compute_lps(pat,pat_len,lps):
    i=1
    len=0
    while i <pat_len:
        if pat[i]==pat[len]:
            len=len+1
            lps[i]=len
            i=i+1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i=i+1
    print(lps)

def kmp(st,pat):
    pat_len=len(pat)
    str_len=len(st)
    lps=[0]*pat_len
    compute_lps(pat,pat_len,lps)
    i=0
    j=0
    while i<str_len:
        if st[i]==pat[j]:
            i=i+1
            j=j+1
        if j==pat_len:
            print("Index Found")
        if i<str_len and st[i]!=pat[j]:
            if j!=0:
                j=lps[j]
            else:
                i=i+1


st=""
pat="AAACAAAA"
kmp(st,pat)