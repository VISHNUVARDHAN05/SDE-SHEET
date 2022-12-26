def myAtoi(s):
    res = 0
    sign=1
    index=0
    n=len(s)
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)
    while index<n and s[index]==" ":
        index=index+1
    if index<n and s[index]=="+":
        sign=1
        index=index+1
    else:
        sign=-1
        index=index+1
    while index<n and s[index].isdigit():
        digit=int(s[index])
        if (res>INT_MAX//10) or (res==INT_MAX//10 and digit>INT_MAX%10):
            if sign==-1:
                return INT_MIN
            else:
                return INT_MAX
        res=(res*10)+1
        index=index+1

    return sign*res
s="words and 987"
myAtoi(s)