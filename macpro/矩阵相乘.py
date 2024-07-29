matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[1,2,3],[1,2,3],[1,2,3]]
row1 = len(matrix1)
col1 = len(matrix1[0])
row2 = len(matrix2)
col2 = len(matrix2[0])
res = [[0 for _ in range(row1)] for _ in range(col2)]
for i in range(row1):
    for j in range(col1):
        for k in range(col2):
            res[i][j] += matrix1[i][j] * matrix2[j][k]
print(res)

