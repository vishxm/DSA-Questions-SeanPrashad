class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.solve()
    
    def unassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1,-1

    def solve(self):
        row, col = self.unassigned()
        if row == -1 and col == -1: return True
        for num in [str(num) for num in range(1,10)]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False
    
    def isSafe(self, row, col, num):
        boxRow = row-row%3
        boxCol = col-col%3
        if self.checkRow(row, num) and self.checkCol(col, num) and self.checkSquare(boxRow, boxCol, num):
            return True
        return False
    
    def checkRow(self, row, num):
        for j in range(9):
            if self.board[row][j] == num: return False
        return True
    
    def checkCol(self, col, num):
        for i in range(9):
            if self.board[i][col] == num: return False
        return True
    
    def checkSquare(self, row, col, num):
        for i in range(row,row+3):
            for j in range(col, col+3):
                if self.board[i][j] == num: return False
        return True