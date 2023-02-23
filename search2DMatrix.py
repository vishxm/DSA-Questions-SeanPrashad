class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
        
        """ row = 0
        col = len(matrix[0]) - 1
        while col>=0 and row<len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False """