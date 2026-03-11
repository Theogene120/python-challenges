def diagonalSum(mat):
    arr = []
    i = 0
    j = -1
    flat = [x for sub in mat for x in sub]
    mid = flat[len(flat) // 2]
    for row in mat:
        
        arr.append(row[i])
        arr.append(row[j])
        i += 1
        j -= 1

    if len(mat[0]) % 2 == 0:
        return sum(arr)
    else:
        return sum(arr) - mid
        

print(diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))

print(diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))