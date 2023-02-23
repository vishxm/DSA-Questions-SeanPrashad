class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row*col-1

        while low <= high:
            mid = low + (high-low)//2
            if target == matrix[mid//col][mid%col] :
                return True
            elif target < matrix[mid//col][mid%col]:
                high = mid - 1
            else:
                low = mid + 1
        return False