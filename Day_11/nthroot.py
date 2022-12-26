def power(num,n):
    num1=1
    for i in range(n):
        num1=num1*num

    return num1
def nthroot(n,m):
    eps=0.00000000001
    low=1
    high=m
    while (high-low)>eps:
        mid=(low+high)/2
        if power(mid,n)<m:
            low=mid
        else:
            high=mid
    print(low)
n=2
m=16
nthroot(n,m)