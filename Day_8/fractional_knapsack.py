def fractional_knapsack(wt,val,cap):
    knap=[]
    res=0
    for i in range(len(wt)):
        knap.append([wt[i],val[i],val[i]//wt[i]])
    knap.sort(key=lambda x:x[2],reverse=True)
    wt=0
    for i in range(len(knap)):
        if wt==cap:
            break
        if wt+knap[i][0]>cap:
            x=cap-wt
            wt=wt+x
            res=res+x*knap[i][2]
        else:
            res=res+knap[i][1]
            wt=wt+knap[i][0]
    print(res)

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
cap = 50
profit=fractional_knapsack(wt,val,cap)