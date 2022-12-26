def findelement(k,n):
    if n==0:
        return 0,k
    n=n-1
    fact=n
    while k>=fact and n>1:
        fact=fact*(n-1)
        n=n-1
    f_ind=k//fact
    k=k%fact
    return f_ind,k
def kthpermutate(n,k):
    s=set()
    for i in range(1,n+1):
        s.add(i)
    k=k-1
    for i in range(n):
        itr=list(s)
        index,i=findelement(k,n)
        ans=ans+str(itr[index])
        itr.pop()
        s=set(itr)

n=int(input())
k=int(input())
kthpermutate(n,k)