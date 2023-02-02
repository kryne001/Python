class Solution(object):

    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        isZeroCol = False
        isZeroRow = False

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0: isZeroRow = True
                    if j == 0: isZeroCol = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1,row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0
        
        for i in range(1,col):
            if matrix[0][i] == 0:
                for j in range(row):
                    matrix[j][i] = 0

        if isZeroRow == True:
            for i in range(col):
                matrix[0][i] = 0
        if isZeroCol == True:
            for i in range(row):
                matrix[i][0] = 0

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

answer = Solution()
answer.setZeroes(matrix2)

print(answer)