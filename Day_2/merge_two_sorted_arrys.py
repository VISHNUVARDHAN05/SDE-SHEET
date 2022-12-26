
import math
def merge_two_sorted_arrys(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    gap=math.ceil((n1+n2)/2)
    while gap>0:
        i=0
        j=gap
        while j<(n1+n2):
            if j<n1 and arr1[i]>arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]
            elif i<n1 and j>=n1 and arr2[j-n1]<arr1[i]:
                arr1[i],arr2[j-n1]=arr2[j-n1],arr1[i]
            elif i>=n1 and j>=n1 and arr2[j-n1]<arr2[i-n1]:
                arr2[i-n1],arr2[j-n1]=arr2[j-n1],arr2[i-n1]
            i=i+1
            j=j+1
        if gap==1:
            gap=0
        else:
            gap = math.ceil(gap/2)



    print(arr1)
    print(arr2)

arr1 = [1,4,8,10]
arr2 = [2,3,9]
merge_two_sorted_arrys(arr1,arr2)