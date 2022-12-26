def Anagrams(s1,s2):
    d1 = {}
    d2 = {}
    f = 0
    for i in s1:
        if i in d1:
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1

    for i in s2:
        if i in d2:
            d2[i] = d2[i] + 1
        else:
            d2[i] = 1

    for k, v in d1.items():
        if k not in d2 or v != d2[k]:
            f = 1
            break
        else:
            d1[k] = -1
            d2[k] = -1
    if f == 1:
        return False
    for k, v in d1.items():
        if v != -1:
            return False
    for k, v in d2.items():
        if v != -1:
            return False
    return True
s = "rat"
t = "car"
res=Anagrams(s,t)
print(res)