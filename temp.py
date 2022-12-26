from functools import  cmp_to_key
def comp(x,y):
    if x+y>y+x:
        return 1
    elif x+y==y+x:
        return 0
    else:
        return -1
def largest_number(arr):
    l=[]
    for i in arr:
        l.append(str(i))
    l.sort(key=cmp_to_key(comp),reverse=True)
    s=''.join(l)
    print(s)


arr=[3,30,34,5,9]
largest_number(arr)