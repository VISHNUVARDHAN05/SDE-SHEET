from collections import defaultdict
def subarrayXor(arr, n, m):
    HashTable=defaultdict(bool)
    HashTable[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if HashTable[curSum^m]:
            count+=HashTable[curSum^m]
        HashTable[curSum]+=1

    return(count)
arr = [4, 2, 2, 6, 4]
target = 6
res=subarrayXor(arr,5,target)
print(res)