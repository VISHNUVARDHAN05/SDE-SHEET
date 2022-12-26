class Meet:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos


def maxMeeting(l, n):
    ans=[]
    l.sort(key=lambda x:x.end)
    ans.append(l[0].pos)

    diff=l[0].end
    for i in range(1,n):
        if l[i].start>diff:
            ans.append(l[i].pos)
            diff=l[i].end
    return ans

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]  
n = len(s)
l = []
for i in range(n):
    l.append(Meet(s[i], f[i], i+1))

res=maxMeeting(l, n)
print(res)

# This code is contributed by MuskanKalra1