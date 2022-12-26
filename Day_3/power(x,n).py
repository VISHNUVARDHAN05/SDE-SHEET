def power(x,n):
    nn=n
    ans=1
    if nn<0:
        nn=-1*nn
    while nn>0:
        if nn%2==0:
            x=x*x
            nn=nn//2
        else:
            ans=ans*x
            nn=nn-1
    if n<0:
        return 1/ans
    return ans


res=power(10,3)
print(res)