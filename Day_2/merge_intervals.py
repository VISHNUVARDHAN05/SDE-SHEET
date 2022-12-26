def merge_intervals(l):
    l.sort(key=lambda x:x[0])
    temp=[]
    start=l[0][0]
    end=l[0][1]
    print(l)
    for i in l:
        if i[0]<=end:
            end=max(end,i[1])
        else:
            temp.append([start,end])
            start=i[0]
            end=i[1]
    temp.append([start,end])
    return temp

l=[[1,3],[2,6],[8,10],[15,18]]
res=merge_intervals(l)
print(res)