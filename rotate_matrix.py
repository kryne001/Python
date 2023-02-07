import numpy as np

matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix = zip(*matrix)

matrix = list(matrix)

rows = len(matrix)

for i in range(rows):
    matrix[i] = matrix[i][::-1]

print(matrix)