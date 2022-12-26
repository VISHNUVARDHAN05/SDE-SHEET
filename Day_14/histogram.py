def area_histogram(arr):
    stack=[]
    i=0
    max_area=0
    while i<len(arr):
        if len(stack)==0 or arr[i]>arr[stack[-1]]:
            stack.append(i)
            i=i+1
        else:
            x=stack.pop()
            if stack:
                area=arr[x]*(i-stack[-1]-1)
            else:
                area=i
            max_area=max(max_area,area)

    while stack:
        x=stack.pop()
        if stack:
            area=arr[x]*(i-stack[-1]-1)
        else:
            area=i
        max_area=max(max_area,area)
    print(max_area)

hist = [6, 2, 5, 4, 5, 1, 6]
area_histogram(hist)