class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, 0, 0, 0, '', res)
        return res
    
    def dfs(self, n, k, open, close, path, res):
        if open > n or close > n or open < close:
            return
        if k == n:
            res.append(path)
            return
        self.dfs(n, k, open+1, close, path + '(', res)
        self.dfs(n, k+1, open, close+1, path+')', res)