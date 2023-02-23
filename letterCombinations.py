class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberDict = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if len(digits) == 0:
            return res
        self.dfs(digits, 0, numberDict, '', res)
        return res
    
    def dfs(self, digits, index, numberDict, path, res):
        if index >= len(digits):
            res.append(path)
            return
        
        possibleStrokes = numberDict[digits[index]]
        for i in possibleStrokes:
            self.dfs(digits, index+1, numberDict, path+i, res)
            