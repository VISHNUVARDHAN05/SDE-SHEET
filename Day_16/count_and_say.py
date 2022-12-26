def countAndSay(n):
    if n == 1:
        return '1'

    xs = countAndSay(n - 1)

    buf = []

    ch = None
    for x in xs:
        if ch == x:
            n += 1
        else:
            if ch:
                buf.append(str(n))
                buf.append(ch)
            ch = x
            n = 1

    buf.append(str(n))
    buf.append(ch)

    return ''.join(buf)
n=4
res=countAndSay(n)
print(res)