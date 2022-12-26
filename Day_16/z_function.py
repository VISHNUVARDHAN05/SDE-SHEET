def compute(res):
    z=[0]*len(res)
    left=0
    right=0
    print(res)
    for k in range(1,len(res)):
        if k>right:
            left=k
            right=k
            while right<len(res) and res[right]==res[right-left]:
                right=right+1
            z[k]=right-left
            right=right-1
        else:
            k1=k-left
            if z[k1]<right-k+1:
                z[k]=z[k1]
            else:
                left=k
                while right<len(res) and res[right]==res[right-left]:
                    right=right+1
                z[k]=right-left
                right=right-1
    print(z)
def z_function(str,pat):
    res=pat+"$"+str
    z=compute(res)

str="GEEKS FOR GEEKS"
pat= "GEEK"
z_function(str,pat)