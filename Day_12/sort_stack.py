def sort_stack_util(s,ele):
    if len(s)==0 or ele>s[-1]:
        s.append(ele)
        return
    else:
        temp=s.pop()
        sort_stack_util(s,ele)
        s.append(temp)
def sort_stack(arr):
    if len(arr)!=0:
        temp=arr.pop()
        sort_stack(arr)
        sort_stack_util(arr,temp)


s = []
s.append(30)
s.append(-5)
s.append(18)
s.append(14)
s.append(-3)
sort_stack(s)
print(s)