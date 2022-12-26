def balanced_parenthesis(arr):
    stack=[]
    for i in arr:
        if len(stack)==0 and (i=="}" or i==")" or i=="]"):
            return False
        if i=="{" or i=="(" or i=="[":
            stack.append(i)
        else:
            x=stack.pop()
            if x=="{" and i=="}":
                continue
            if x=="(" and i==")":
                continue
            if x=="[" and i=="]":
                continue
    if stack:
        return False
    return True
arr="[()"
res=balanced_parenthesis(arr)
print(res)