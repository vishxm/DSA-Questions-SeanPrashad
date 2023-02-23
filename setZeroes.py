class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowf = False
        colf = False
        rnum = len(matrix)
        cnum = len(matrix[0])

        for i in range(rnum):
            if matrix[i][0] == 0:
                rowf = True
                break
        
        for i in range(cnum):
            if matrix[0][i] == 0:
                colf = True
                break

        for i in range(1,rnum):
            for j in range(1, cnum):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,rnum):
            for j in range(1, cnum):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            
        if rowf:
            for i in range(rnum):
                matrix[i][0] = 0
        
        if colf:
            for i in range(cnum):
                matrix[0][i] = 0
