def search_in_a_2d_matrix(arr,key):
    row_len=len(arr)
    col_len=len(arr[0])
    f=0
    i=0
    j=col_len-1
    while i<row_len and j>=0:
        if arr[i][j]==key:
            f=1
            break
        elif key>arr[i][j]:
            i=i+1
        elif key<arr[i][j]:
            j=j-1

    if f==0:
        print("Element Not Found in 2-D Array ")
    else:
        print("Element  Found in 2-D Array At {},{}".format(i,j))




arr=[[10,20,30,40],[15,25,35,45],[27,29,237,48],[32,33,39,50]]
search_in_a_2d_matrix(arr,29)

