class Solution:
    # space optimised
    def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
        import itertools
        dp = [1]*n
        for i, j in itertools.product(range(1,m), range(1,n)):
            dp[j] += dp[j-1]
        return dp[-1]
    """ 
    # math solution
    def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
        return self.fact(m+n-2)//self.fact(m-1)//self.fact(n-1)

    def fact(self,i):
        if i <= 1: return 1
        return i*self.fact(i-1) """    

    """ # recursion with memoisation
        @cache 
        def dfs(i,j):
            if i>=m or j>=n: return 0
            if i==m-1 and j==n-1: return 1
            return dfs(i+1,j)+dfs(i,j+1)
        return dfs(0,0) """
    
    """ 
        #recursion
        if i>=m or j>=n: return 0
        if i==m-1 and j==n-1: return 1
        return self.uniquePaths(m,n,i+1,j)+ self.uniquePaths(m,n,i,j+1) """