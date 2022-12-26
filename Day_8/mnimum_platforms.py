def minimum_platforms(arr,dep):
    arr.sort()
    dep.sort()
    n=len(arr)
    i=1
    j=0
    plat=1
    max_p=1
    while i<n and j<n:
        if arr[i]<=dep[j]:
            plat=plat+1
            i=i+1
        elif arr[i]>dep[j]:
            plat=plat-1
            j=j+1
        if plat>max_p:
            max_p=plat
    print(max_p)







arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
minimum_platforms(arr,dep)