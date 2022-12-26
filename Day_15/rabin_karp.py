def rabin_karp(st,pat):
    d= {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    pat_len=len(pat)
    p=5381
    pat_hash=0
    l=[]
    str_len=len(st)
    for i in range(pat_len):
        #print(pow(26,pat_len-i-1))
        temp=d[pat[i]]*pow(26,pat_len-i-1)
        temp=temp%p
        pat_hash=pat_hash+temp
    win_hash=0
    win_str=""
    for i in range(pat_len):
        #print(pow(26,pat_len-i-1))
        temp=d[st[i]]*pow(26,pat_len-i-1)
        temp=temp%p
        win_hash=win_hash+temp
        win_str=win_str+st[i]
    ind=0
    if pat_hash==win_hash:
        return True
    for i in range(pat_len,str_len):
        temp=(d[win_str[0]])*(pow(26,pat_len-1))
        win_hash=win_hash-temp
        win_str=win_str[1:]
        win_hash=win_hash*26
        win_hash=win_hash+(d[st[i]]*pow(26,0))
        win_str=win_str+st[i]
        ind=ind+1
        if win_hash==pat_hash:
            l.append(ind)
    print(l)
    return False


st="cdabcdabcbabc"
pat="abc"
res=rabin_karp(st,pat)
print(res)

