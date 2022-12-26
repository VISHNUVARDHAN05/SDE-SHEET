import math


def Majority(arr):
    #if we need to find majority for n/3 will get max 2 elements
    c1=0
    c2=0
    ele1=-1
    ele2=-1
    i=0
    while i<len(arr):
        if ele1==arr[i]:
            c1=c1+1
        elif ele2==arr[i]:
            c2=c2+1
        elif c1==0:
            ele1=arr[i]
            c1=c1+1
        elif c2==0:
            ele2=arr[i]
            c2=c2+1
        else:
            c1=c1-1
            c2=c2-1
        i=i+1

    count_ele1=arr.count(ele1)
    count_ele2 = arr.count(ele2)
    len_arr=len(arr)
    if count_ele1>=int(math.ceil(len_arr/3)) and count_ele2>=int(math.ceil(len_arr/3)):
        return [ele1,ele2]
    if count_ele1>=int(math.ceil(len_arr/3)):
        return [ele1]
    if count_ele2>=int(math.ceil(len_arr/3)):
        return [ele2]
arr=[1,1,1,3,3,2,2,2]
res=Majority(arr)
print(res)