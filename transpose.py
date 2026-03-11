def transpose(matrix):

    res = []
    n = len(matrix)
    subN = len(matrix[0])
    i = 0
    j = 0

    for i in range(subN):
        temp = []
        for j in range(n):
            temp.append(matrix[j][i])
        res.append(temp)
    
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

    