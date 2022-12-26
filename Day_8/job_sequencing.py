def job_sequencing(jobs,n):
    jobs.sort(key=lambda x:x[2],reverse=True)
    maxi=0
    profit=0
    for i in jobs:
        maxi=max(maxi,i[1])
    res=[-1]*maxi
    for i in range(len(jobs)):
        for j in range(jobs[i][1]-1,-1,-1):
            if res[j]==-1:
                res[j]=jobs[i][0]
                profit=profit+jobs[i][2]
                break
    print(profit)


n = 4
jobs= [[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
job_sequencing(jobs,n)