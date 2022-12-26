import math
def heapify(arr,ind):
    largest=ind
    left=(2*ind)+1
    right = (2 * ind) + 2
    if left<len(arr) and arr[left] > arr[largest]:
        largest=left
    else:
        largest=ind
    if right < len(arr) and arr[right] > arr[largest]:
        largest= right
    if largest != ind:
        arr[ind],arr[largest] = arr[largest],arr[ind]
        heapify(arr, largest)



def percolate_up(arr,ind):
    parent=(ind-1)//2
    while ind>0 and arr[parent]<arr[ind]:
        arr[ind],arr[parent] = arr[parent],arr[ind]
        ind=parent
        parent = (ind-1) // 2



#arr=[1,3,5,4,6,13,10,9,8,15,17]
arr=[1,2,3,4,5,6]
n=len(arr)
for i in range((n//2)-1,-1,-1):
    heapify(arr,i)
print(arr)
arr.append(7)
n=n+1
percolate_up(arr,n-1)
print(arr)