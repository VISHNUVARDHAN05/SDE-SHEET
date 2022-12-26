
def setZeroes(List):
    col = True
    for i in range(len(List)):
        if List[i][0] == 0:
            col = False
        for j in range(1, len(List[0])):
            if List[i][j] == 0:
                List[i][0] = 0
                List[0][j] = 0

    for i in range(len(List) - 1, -1, -1):
        for j in range(len(List[0]) - 1, 0, -1):
            if List[i][0] == 0 or List[0][j] == 0:
                List[i][j] = 0
        if col == False:
            List[i][0] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)