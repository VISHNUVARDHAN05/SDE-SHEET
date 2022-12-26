def Print_Pascal_Triangle(n):
    l=[]
    res=[]
    temp=[]
    for i in range(1,n+1):
        temp=[]
        for j in range(i):
            if j==0 or j==i-1:
                temp.append(1)
            else:
                temp.append(res[j]+res[j-1])
        res=temp
        l.append(res)
    return l




def print_number_pascal_triangle(r,c):
    res=1
    for i in range(c):
        res=res*(r-i)
    for i in range(c,1,-1):
        res=res//i
    return res



def print_row_pascal(n):
    for i in range(n):
        if i==0 or i==n-1:
            print(1)
        else:
            res=res


res=Print_Pascal_Triangle(5)
print(res)