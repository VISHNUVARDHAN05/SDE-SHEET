def find_duplicate(arr):
    slow=arr[0]
    fast=arr[arr[0]]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[arr[fast]]
    fast=0
    while fast!=slow:
        slow=arr[slow]
        fast=arr[fast]

    return fast



arr=[1,3,4,2,2]
res=find_duplicate(arr)
print(res)