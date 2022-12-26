def missing_and_repeating(arr):
    xor=0
    for i in range(1,len(arr)+1):
        xor=xor^i
    for i in arr:
        xor=xor^i
    x=0
    y=0
    set_bit=xor & ~(xor-1)
    for i in range(1,len(arr)+1):
        if i&set_bit!=0:
            x=x^i
        else:
            y=y^i


    for i in arr:
        if i&set_bit!=0:
            x=x^i
        else:
            y=y^i
    return x,y

arr=[3,1,2,5,3]
x,y=missing_and_repeating(arr)

print(x,y)