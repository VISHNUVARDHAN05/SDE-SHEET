def minimum_coins(coins,val):
    c=0
    for i in range(len(coins)-1,-1,-1):
        while val>=coins[i]:
            c=c+1
            val=val-coins[i]
            print(coins[i])
    print(c)
coins=[1,2,5,10,20,50,100,500,1000]
val = 70
minimum_coins(coins,val)
