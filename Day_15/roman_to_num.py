def romanToInt(s):
    roman = {'O':0,'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    res=0
    s=s[::-1]+"O"
    print(s)
    i=0
    n=len(s)
    while i<n-1:
        if roman[s[i]]<=roman[s[i+1]]:
            res=res+roman[s[i]]
            i=i+1
        else:
            res = res + roman[s[i]]-roman[s[i+1]]
            i=i+2

    print(res)

s="IV"
romanToInt(s)
