print("First Matrix: ")
a = [[1,2,3],
     [2,3,4],
     [3,4,5]]
for f in a:
     print(f)
print("\nSecond Matrix: ")
b = [[4,5,6],
     [5,6,7],
     [6,7,8]]
for s in b:
     print(s)
print("\nAfter subtraction of a & b Matrix")
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(a)):
     for j in range(len(a[0])):
          result[i][j] = a[i][j] - b[i][j]
for r in result:
     print(r)