
def reverse(n,ind1,ind2):
    ind1=ind1+1
    num_len=len(n)
    while ind1<num_len:
        if ind1>=num_len:
            break
        n[ind1],n[num_len-1]=n[num_len-1],n[ind1]
        ind1=ind1+1
        num_len=num_len-1
    return n

def next_permutation(n):
    if len(n)<=1:
        return None
    ind1=0
    ind2=0
    i=len(n)-2
    while i>=0:
        if n[i]<n[i+1]:
            ind1=i
            break
        i=i-1
    i=len(n)-1
    if ind1>0:
        while i>=0:
            if n[i]>n[ind1]:
                ind2=i
                print(n[ind2])
                break
            i=i-1
        n[ind1],n[ind2]=n[ind2],n[ind1]
    res=reverse(n,ind1+1,ind2)
    return res


res=next_permutation([1,3,5,4,2])
print(res)