def nge(arr):
    n=len(arr)
    temp=[]
    temp.insert(0,-1)
    stack=[]
    stack.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if stack:
            if stack[-1]>arr[i]:
                temp.insert(0,stack[-1])
                stack.append(arr[i])
            else:
                while len(stack)!=0:
                    if not stack[-1] > arr[i]:
                        stack.pop()
                    else:
                        break

                if len(stack)==0 and i==0:
                    temp.insert(0, -1)
                    break
                if len(stack) == 0:
                    stack.append(arr[i])
                    temp.insert(0,-1)
                temp.insert(0, stack[-1])
                stack.append(arr[i])

        else:
            stack.append(arr[i])

    print(temp)
arr=[13,7,6,12]
arr2=[4,5,2,25]
nge(arr2)