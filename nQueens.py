class Solution:
    board = [['.' for _ in range(9)] for _ in range(9)]
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        for i in range(n):
            for j in range(n):
                self.solve(i,j, res)
        return res

    def solve(self, row, col, res):
        if row >= self.n:
            res.append(self.board)
            return
        for i in range(self.n):
            for j in range(self.n):
                if self.check(i,j):
                    self.board[i][j] = 'Q'
                    self.solve(i+1, 0, res)    

    def check(self, row, col):
        rowCheck = True
        for i in range(self.n):
            if self.board[i][col] != '.':
                rowCheck = False
                break
        colCheck = True
        for j in range(self.n):
            if self.board[row][j] != '.':
                colCheck = False
                break
        return rowCheck and colCheck
    
fourQueen = Solution()
print(fourQueen.solveNQueens(4))