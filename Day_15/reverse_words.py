def reverse_words(str):
    res=""
    temp=""
    f=0
    for i in range(len(str)):
        if i==len(str)-1:
            temp=temp+str[i]
            break
        if str[i]==" ":
            f=1
            res=temp+" "+res
            temp=""
        else:
            temp=temp+str[i]
    if f==0:
        res=temp
    else:
        res=temp+" "+res
    print(res)
s="amazing"
reverse_words(s)