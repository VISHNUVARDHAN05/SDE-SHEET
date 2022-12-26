def get_prefix(s1,s2):
    i=0
    j=0
    n1=len(s1)
    n2=len(s2)
    while i<n1 and j<n2:
        if s1[i]!=s2[j]:
            break
        i=i+1
        j=j+1
    return s1[:i]

def longest_common_prefix(arr):
    strs.sort(key=len)
    prefix = arr[0]
    shortest = min(strs, key=len)

    n=len(arr)
    for i in range(1,n):
        prefix=get_prefix(prefix,arr[i])


strs = ["ab", "a"]
longest_common_prefix(strs)