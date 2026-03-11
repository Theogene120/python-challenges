def transpose(matrix):

    res = []
    n = len(matrix)
    subN = len(matrix[0])
    i = 0
    j = 0

    for i in range(n):
        temp = []
        for j in range(subN):
            temp.append(matrix[i,j])
        res.append(temp)
    
    return temp

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

    