# def setZeroes(matrix):
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     idx1=0
#     idx2=0
#     for i, arr in enumerate(matrix):
#         if 0 in arr:
#             idx1 = i
#         for j, num in enumerate(arr):
#             if num == 0:
#                 idx2 = j
#     for i in range(len(matrix[idx1])):
#         matrix[idx1][i] = 0
#     for x, arr in enumerate(matrix):
#         for y, n in enumerate(num):
#             if y == idx2:
#                 matrix[x][y] = 0

def setZeroes(matrix):
    rows = set()
    cols = set()

    # Step 1: record rows & columns with zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Step 2: zero out rows
    for r in rows:
        for j in range(len(matrix[0])):
            matrix[r][j] = 0

    # Step 3: zero out columns
    for c in cols:
        for i in range(len(matrix)):
            matrix[i][c] = 0

    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))