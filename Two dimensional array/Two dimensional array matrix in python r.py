matrix1 = [[1,2,3],
           [2,3,4],
           [3,4,5]]
for i in matrix1:
    print(i)
print()
matrix2 = [[5,6,7],
           [6,7,8],
           [7,8,9]]
for j in matrix2:
    print(j)
print("After multiplication matrix1 & matrix2")
matrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for a in range(len(matrix1)):
    for b in range(len(matrix2[0])):
        for c in range(len(matrix)):
            matrix[a][b] = matrix[a][b] + matrix1[a][c] * matrix2[c][b]
for r in matrix:
    print(r)
