def longest_consequence(arr):
    d={}
    mc=0
    for i in arr:
        d[i]=True
    for i in range(len(arr)):
        x=arr[i]
        if not x-1 in d:
            y=x
            c=1
            while y+1 in d:
                c=c+1
                y=y+1
            mc=max(mc,c)
    print(mc)

arr=[3,8,5,7,6]
longest_consequence(arr)
