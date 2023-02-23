class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(s,i):
            if i == len(s): 
                self.res.append(s)
            else:
                if s[i].isalpha():
                    temp = [ch for ch in s]
                    temp[i] = temp[i].upper()
                    dfs("".join(temp), i+1)
                    temp[i] = temp[i].lower()
                    dfs("".join(temp), i+1)
                else:
                    dfs(s, i+1)

        dfs(s,0)
        return res