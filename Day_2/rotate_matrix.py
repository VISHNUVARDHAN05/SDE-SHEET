def rotate_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j]=arr[j][i]

    print(arr)

    for i in range(len(arr)):
        for j in range(len(arr)//2):
            arr[i][j],arr[i][len(arr[0])-1-j]=arr[i][len(arr[0])-1-j],arr[i][j]

l=[[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(l)
print(l)