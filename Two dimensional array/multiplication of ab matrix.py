matrix1 = [[1,2,3],
           [2,3,4],
           [3,4,5]]
for i in matrix1:
    print(i)
print()
matrix2 = [[4,5,6],
           [5,6,7],
           [7,8,9]]
for j in matrix2:
    print(j)
Result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
e = len(matrix1)
print(e)
f = len(matrix1[0])
print(f)
for a in range(e):
    for b in range(f):
        for c in range(len(Result)):
            Result[a][b] = Result[a][b] + (matrix1[a][c] * matrix2[c][b])
for r in Result:
    print(r)
